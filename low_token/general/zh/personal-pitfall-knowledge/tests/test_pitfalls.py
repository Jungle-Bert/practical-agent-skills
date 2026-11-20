import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('pitfalls', Path(__file__).parents[1] / 'scripts/pitfalls.py')
pitfalls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pitfalls)


class PitfallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'entries').mkdir()
        self.rows = []
        self.add('PIT-001-pdb', ['C1041', 'PDB', '文件锁', 'MSVC'], 'Check the owning process.', 'Confirmed')
        self.add('PIT-002-encoding', ['MSVC', '中文编码', 'syntax error', 'C4819'], 'Inspect preprocessor output.', 'Confirmed')
        self.add('PIT-003-wfi', ['WFI', '唤醒', 'UART'], 'Inspect interrupt routing.', 'Hardware pending')
        self.save()

    def add(self, entry_id, terms, direction, status):
        content = f'# {entry_id}\n\n{direction}\nHardware result: {status}.\n'
        path = f'entries/{entry_id}.md'
        (self.root / path).write_text(content, encoding='utf-8')
        self.rows.append(dict(id=entry_id, title=entry_id, keywords=terms, direction=direction,
                              scope='Only the specified environment.', status=status, path=path,
                              sha256=hashlib.sha256((self.root / path).read_bytes()).hexdigest()))

    def save(self):
        (self.root / 'index.jsonl').write_text(''.join(json.dumps(row) + '\n' for row in self.rows), encoding='utf-8')

    def test_error_code_beats_shared_component(self):
        result = pitfalls.search(self.root, 'MSVC C1041 中文编码')
        self.assertTrue(result.startswith('PIT-001-pdb'))

    def test_chinese_and_english_aliases(self):
        self.assertIn('PIT-002-encoding', pitfalls.search(self.root, '发生中文编码问题'))
        self.assertIn('PIT-002-encoding', pitfalls.search(self.root, 'MSVC syntax error'))

    def test_specific_match_omits_weak_component_matches(self):
        result = pitfalls.search(self.root, 'MSVC C1041')
        self.assertIn('PIT-001-pdb', result)
        self.assertNotIn('PIT-002-encoding', result)

    def test_search_never_reads_card_bodies(self):
        with patch.object(Path, 'read_bytes', side_effect=AssertionError('Card read')), \
             patch.object(Path, 'read_text', side_effect=AssertionError('Full file read')):
            self.assertIn('PIT-001-pdb', pitfalls.search(self.root, 'C1041'))
            self.assertEqual('NO_MATCH', pitfalls.search(self.root, 'unrelated database error'))

    def test_no_match_does_not_fall_back_to_details(self):
        self.assertEqual('NO_MATCH', pitfalls.search(self.root, 'unrelated database error'))

    def test_short_alias_respects_word_boundaries(self):
        self.assertFalse(pitfalls.contains('windows', 'do'))
        self.assertTrue(pitfalls.contains('DO 响应延迟', 'do'))

    def test_pending_state_preserved(self):
        self.assertIn('Hardware pending', pitfalls.search(self.root, 'WFI'))

    def test_output_budgets_and_truncation(self):
        result = pitfalls.search(self.root, 'MSVC WFI', max_chars=128)
        self.assertLessEqual(len(result), 128)
        self.assertIn('TRUNCATED', result)
        card = self.root / self.rows[0]['path']
        card.write_text('x' * 10000, encoding='utf-8')
        self.rows[0]['sha256'] = hashlib.sha256(card.read_bytes()).hexdigest()
        self.save()
        self.assertLessEqual(len(pitfalls.get(self.root, self.rows[0]['id'], 1600)), 1600)

    def test_get_reads_only_selected_card(self):
        target = self.root / self.rows[0]['path']
        original = Path.read_bytes
        reads = []
        def read(path):
            reads.append(path)
            return original(path)
        with patch.object(Path, 'read_bytes', read):
            self.assertIn('owning process', pitfalls.get(self.root, self.rows[0]['id']))
        self.assertEqual([target.resolve()], reads)

    def test_stale_metadata_blocks_unverified_reuse(self):
        (self.root / self.rows[0]['path']).write_text('changed', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'STALE_INDEX'):
            pitfalls.get(self.root, self.rows[0]['id'])

    def test_index_update_preserves_other_records(self):
        row = dict(self.rows[0], direction='Check current lock owner.')
        metadata = self.root / 'metadata.json'
        metadata.write_text(json.dumps(row), encoding='utf-8')
        self.assertIn('INDEXED', pitfalls.update_index(self.root, metadata))
        rows = pitfalls.load_index(self.root)
        self.assertEqual(3, len(rows))
        self.assertEqual(self.rows[1:], rows[1:])
        self.assertFalse((self.root / '.index.lock').exists())

    def test_busy_lock_does_not_overwrite_index(self):
        metadata = self.root / 'metadata.json'
        metadata.write_text(json.dumps(self.rows[0]), encoding='utf-8')
        before = (self.root / 'index.jsonl').read_bytes()
        (self.root / '.index.lock').touch()
        with self.assertRaisesRegex(ValueError, 'INDEX_BUSY'):
            pitfalls.update_index(self.root, metadata)
        self.assertEqual(before, (self.root / 'index.jsonl').read_bytes())

    def test_duplicate_ids_and_escaping_paths_rejected(self):
        self.rows.append(self.rows[0])
        self.save()
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            pitfalls.search(self.root, 'C1041')
        with self.assertRaisesRegex(ValueError, 'path'):
            pitfalls.entry_path(self.root, dict(self.rows[0], path='../outside.md'))


if __name__ == '__main__':
    unittest.main()
