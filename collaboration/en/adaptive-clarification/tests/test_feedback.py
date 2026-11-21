import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("feedback", Path(__file__).parents[1] / "scripts/feedback.py")
feedback = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feedback)


class FeedbackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = feedback.store_path(self.root, "project-a/task-one")

    def entry(self, **changes):
        result = {
            "id": "runtime", "question": "Which runtime?", "value": "Possibly Python",
            "status": "uncertain", "source_kind": "user", "source": "User reply",
        }
        result.update(changes)
        return result

    def test_correction_keeps_old_uncertainty_and_other_items(self):
        feedback.save_entry(self.path, "project-a/task-one", self.entry())
        feedback.save_entry(self.path, "project-a/task-one", self.entry(id="deadline", value="Friday", status="stated"))
        feedback.save_entry(self.path, "project-a/task-one", self.entry(value="Python 3.11", status="stated", reason="User corrected the version"))
        state = feedback.read_state(self.path, "project-a/task-one")
        self.assertEqual(state["items"]["runtime"]["status"], "stated")
        self.assertEqual(state["items"]["deadline"]["value"], "Friday")
        self.assertEqual(state["history"][-1]["previous"]["status"], "uncertain")
        self.assertIn("corrected", state["history"][-1]["reason"])

    def test_refusal_and_user_completion_do_not_store_answers(self):
        for status in ("declined", "user_fill"):
            with self.subTest(status=status):
                with self.assertRaises(ValueError):
                    feedback.save_entry(self.path, "project-a/task-one", self.entry(status=status))
                feedback.save_entry(self.path, "project-a/task-one", self.entry(id=status, status=status, value=None))
        self.assertIsNone(feedback.read_state(self.path, "project-a/task-one")["items"]["declined"]["value"])

    def test_delegation_draft_and_assumption_stay_distinct(self):
        for status, source in (("delegated", "user"), ("draft", "ai"), ("assumed", "ai")):
            feedback.save_entry(self.path, "project-a/task-one", self.entry(id=status, status=status, source_kind=source))
        state = feedback.read_state(self.path, "project-a/task-one")
        self.assertEqual({row["status"] for row in state["items"].values()}, {"delegated", "draft", "assumed"})
        with self.assertRaises(ValueError):
            feedback.save_entry(self.path, "project-a/task-one", self.entry(status="stated", source_kind="ai"))

    def test_verification_requires_provenance_and_evidence(self):
        with self.assertRaises(ValueError):
            feedback.save_entry(self.path, "project-a/task-one", self.entry(status="verified"))
        with self.assertRaises(ValueError):
            feedback.save_entry(self.path, "project-a/task-one", self.entry(status="verified", source_kind="verification"))
        feedback.save_entry(self.path, "project-a/task-one", self.entry(status="verified", source_kind="verification", evidence="Successful runtime command in this task"))

    def test_contexts_are_isolated_and_reads_do_not_create_files(self):
        feedback.save_entry(self.path, "project-a/task-one", self.entry())
        other = feedback.store_path(self.root, "project-b/task-one")
        self.assertEqual(feedback.summary(other, "project-b/task-one"), "NO_RECORDS")
        self.assertFalse(other.parent.exists())
        self.assertNotEqual(self.path, other)
        with self.assertRaises(ValueError):
            feedback.read_state(self.path, "project-b/task-one")

    def test_summary_is_bounded_and_excludes_history(self):
        feedback.save_entry(self.path, "project-a/task-one", self.entry(value="OLD_PRIVATE_VALUE"))
        feedback.save_entry(self.path, "project-a/task-one", self.entry(value="新" * 2000, reason="New answer"))
        result = feedback.summary(self.path, "project-a/task-one", max_chars=220)
        self.assertLessEqual(len(result), 220)
        self.assertIn("TRUNCATED", result)
        self.assertNotIn("OLD_PRIVATE_VALUE", result)

    def test_private_root_rejects_repository_and_skill_locations(self):
        for marker in (".git", "SKILL.md"):
            parent = self.root / marker.replace(".", "_")
            parent.mkdir()
            (parent / marker).touch()
            with self.assertRaises(ValueError):
                feedback.store_path(parent / "data", "task")

    def test_repository_storage_requires_opt_in_and_preserves_revisions(self):
        for git_is_file in (False, True):
            with self.subTest(git_is_file=git_is_file):
                project = self.root / ("worktree" if git_is_file else "repository")
                project.mkdir()
                marker = project / ".git"
                marker.touch() if git_is_file else marker.mkdir()
                with self.assertRaises(ValueError):
                    feedback.store_path(project / ".agent-feedback", "task")
                path = feedback.store_path(project / ".agent-feedback", "task", allow_repository=True)
                feedback.save_entry(path, "task", self.entry())
                feedback.save_entry(path, "task", self.entry(value="Confirmed Python", status="stated", reason="User confirmed"))
                state = feedback.read_state(path, "task")
                self.assertEqual(state["revision"], 2)
                self.assertEqual(state["history"][-1]["previous"]["status"], "uncertain")
                self.assertTrue(path.is_relative_to(project.resolve()))

    def test_repository_opt_in_never_allows_skill_folder_storage(self):
        (self.root / "SKILL.md").touch()
        with self.assertRaises(ValueError):
            feedback.store_path(self.root / "data", "task", allow_repository=True)

    def test_failed_replace_preserves_old_state_and_cleans_own_lock(self):
        feedback.save_entry(self.path, "project-a/task-one", self.entry())
        before = self.path.read_bytes()
        with patch.object(feedback.os, "replace", side_effect=OSError("Disk failure")):
            with self.assertRaises(OSError):
                feedback.save_entry(self.path, "project-a/task-one", self.entry(value="changed", reason="Correction"))
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual({path.name for path in self.path.parent.iterdir()}, {"feedback.json"})

    def test_existing_lock_is_not_removed_or_overwritten(self):
        self.path.parent.mkdir(parents=True)
        lock = self.path.with_suffix(".lock")
        lock.write_text("another writer", encoding="utf-8")
        with self.assertRaises(ValueError):
            feedback.save_entry(self.path, "project-a/task-one", self.entry())
        self.assertEqual(lock.read_text(encoding="utf-8"), "another writer")
        self.assertFalse(self.path.exists())

    def test_forget_removes_target_history_and_preserves_other_feedback(self):
        feedback.save_entry(self.path, "project-a/task-one", self.entry(value="sensitive old answer"))
        feedback.save_entry(self.path, "project-a/task-one", self.entry(value="corrected answer", reason="Correction"))
        feedback.save_entry(self.path, "project-a/task-one", self.entry(id="other"))
        self.assertTrue(feedback.forget_entry(self.path, "project-a/task-one", "runtime"))
        state = feedback.read_state(self.path, "project-a/task-one")
        self.assertNotIn("runtime", state["items"])
        self.assertIn("other", state["items"])
        self.assertNotIn("sensitive old answer", json.dumps(state))
        self.assertNotIn("corrected answer", json.dumps(state))

    def test_corrupt_store_and_revision_without_reason_are_preserved(self):
        feedback.save_entry(self.path, "project-a/task-one", self.entry())
        before = self.path.read_bytes()
        with self.assertRaises(ValueError):
            feedback.save_entry(self.path, "project-a/task-one", self.entry(value="new"))
        self.assertEqual(self.path.read_bytes(), before)
        self.path.write_text('{"version": 1, "items": []}', encoding="utf-8")
        corrupt = self.path.read_bytes()
        with self.assertRaises(ValueError):
            feedback.save_entry(self.path, "project-a/task-one", self.entry(reason="Correction"))
        self.assertEqual(self.path.read_bytes(), corrupt)

    def test_identifier_and_output_budget_are_checked(self):
        with self.assertRaises(ValueError):
            feedback.save_entry(self.path, "project-a/task-one", self.entry(id="../outside"))
        with self.assertRaises(ValueError):
            feedback.summary(self.path, "project-a/task-one", max_chars=10)

    def test_summary_does_not_let_a_long_answer_hide_other_decisions(self):
        feedback.save_entry(self.path, "project-a/task-one", self.entry(id="deadline", value="Friday"))
        feedback.save_entry(self.path, "project-a/task-one", self.entry(value="long answer " * 150))
        result = feedback.summary(self.path, "project-a/task-one")
        self.assertIn('"id": "deadline"', result)
        self.assertIn('"id": "runtime"', result)
        detail = feedback.summary(self.path, "project-a/task-one", "runtime", max_chars=8000)
        self.assertIn("long answer " * 150, detail)

    def test_cli_records_reads_and_forgets(self):
        entry_path = self.root / "entry.json"
        entry_path.write_text(json.dumps(self.entry()), encoding="utf-8")
        base = [sys.executable, "-X", "utf8", str(Path(feedback.__file__)), "--root", str(self.root), "--context", "cli-task"]
        for command, expected in ((["record", "--entry", str(entry_path)], "RECORDED runtime"),
                                  (["show", "--id", "runtime"], "Possibly Python"),
                                  (["forget", "--id", "runtime"], "FORGOTTEN runtime"),
                                  (["show"], "NO_RECORDS")):
            result = subprocess.run(base + command, capture_output=True, encoding="utf-8")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(expected, result.stdout)

    def test_cli_repository_choice_gate(self):
        (self.root / ".git").mkdir()
        entry_path = self.root / "entry.json"
        entry_path.write_text(json.dumps(self.entry()), encoding="utf-8")
        base = [sys.executable, "-X", "utf8", str(Path(feedback.__file__)), "--root", str(self.root / "data"), "--context", "task"]
        denied = subprocess.run(base + ["record", "--entry", str(entry_path)], capture_output=True, encoding="utf-8")
        self.assertNotEqual(denied.returncode, 0)
        self.assertFalse((self.root / "data").exists())
        allowed = subprocess.run(base + ["--allow-repository", "record", "--entry", str(entry_path)], capture_output=True, encoding="utf-8")
        self.assertEqual(allowed.returncode, 0, allowed.stderr)
        shown = subprocess.run(base + ["--allow-repository", "show"], capture_output=True, encoding="utf-8")
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertIn("Possibly Python", shown.stdout)


if __name__ == "__main__":
    unittest.main()
