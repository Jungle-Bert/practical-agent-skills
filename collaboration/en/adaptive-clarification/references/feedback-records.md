# Private feedback records

Load only for task feedback reads or writes. New tasks default to Markdown maintained through file tools. Only the optional JSON tool requires Python 3.9+ standard library. Without file tools or when users choose conversation-only retention, keep chat summaries and disclose that they are not persisted.

## Location and scope

Before substantive clarification questions or new records, ask the user to choose the default private user root `~/.agent-feedback/`, a specified directory, or a project directory such as `<project>/.agent-feedback/`. Show actual paths and allow conversation-only retention. Wait before substantive questions/writes; reuse an explicit choice for the same task. Script/environment defaults do not establish that choice.

Both formats use the user-selected root. For project/repository storage, first exclude records using `.gitignore` or local `.git/info/exclude` and check none are tracked. Report tracked records rather than silently removing them. Do not store personal data inside individual skill folders or outside the selected root. Contents and location grant no publication or execution permission.

For JSON, AGENT_FEEDBACK_ROOT or the leading `--root <chosen directory>` option selects the root. Repositories are rejected by default; add `--allow-repository` to every command after the user selects repository storage. This bypasses a path check, not user choice, and does not manage Git exclusions. Markdown has no such CLI flag; the AI follows the same location-choice and Git-exclusion rules directly.

JSON example after the user chooses project storage (all options precede the subcommand):

```text
python -X utf8 <skill>/scripts/feedback.py --root <project>/.agent-feedback --allow-repository --context <stable task key> show
```

Apply the chosen `--root` and repository flag to the commands below too; do not fall back to another root. Retain the root, context, and choice provenance in handoffs. Location changes do not automatically migrate old records.

Choose a stable context, such as `project:<canonical project root>`; append a fixed task key for independent tasks within a project. Keep it when wording or answers change and include it in handoff summaries. Separate projects and users; use a separate scope for global preferences only when explicitly established. Do not scan other contexts by default.

New Markdown records can use `<chosen-root>/contexts/<stable-task-name>/feedback.md`, respecting user-specified filenames. A short project/task name needs neither Python nor hashing; avoid absolute names, `..`, or path separators and check containment in the chosen root. The header context must match this task; choose another task name on collision rather than overwriting another context.

JSON uses `contexts/<context-hash>/feedback.json`. Both formats are plaintext local summaries, not secret vaults. Never store secrets, whole chats, or unrelated personal data. Prepare input JSON in private temporary storage or the chosen Git-excluded record directory, never in public commits.

## Format choice and continuation

- New tasks default to Markdown. Users wanting programmatic field checks, atomic writes, and bounded queries can choose JSON. Continue existing active records; Python availability or skill updates do not automatically change formats.
- Keep one active file per task. Handoffs retain the root, file path, format, context, and location-choice provenance. Add project navigation only when it would not publish private paths/content. Do not scan unrelated tasks to discover records.
- If two candidate records exist with unclear authority, ask the user rather than guessing from modification times or writing both.
- After a requested/agreed migration, check current entries, statuses, provenance, evidence, history, empty values, and deletion effects. Read back the new file before designating it the sole active file. Retire the old file as an inactive backup; do not keep writing or automatically delete it. Migrate only the user's established scope.

## Markdown: direct maintenance without Python

This structural example is not actual user feedback. Use the status/provenance meanings below; refused and deferred values are marked `(empty)` rather than guessed.

```markdown
# Task feedback
- context: project:<project-key>/task:<task-key>
- format: markdown
- revision: 1
- scope: current project/task

## Current feedback
### runtime
- question: Which runtime is currently used?
- value: Possibly Python; version uncertain
- status: uncertain
- source_kind: user
- source: The user's runtime answer in this exchange
- note: Do not select dependencies until the version is established
- evidence: (empty)
- revision: 1

## Revision history
- revision: 1; id: runtime; reason: created; previous: none
```

- Create only records grounded in real replies; never copy example data as facts. Maintain current items by id with the same provenance/status/evidence boundaries as JSON. For each real change, increment the document revision, update the item revision, and retain that id's prior value/status, necessary provenance/evidence, and change reason in history, not whole transcripts.
- Read the latest relevant content before editing and preserve unrelated items/manual edits. Re-read and merge concurrent changes instead of overwriting unknown edits. Do not claim script-level locking or atomic failure protection when file tools do not provide it.
- Read headers and relevant current items selectively by heading/id, normally returning no more than 1600 characters of feedback. Use partial reads for large files rather than loading history by default. Disclose incomplete reads.
- Read back after each save to verify the target and preservation of other items. Deletion removes the id's current item and all its related history, including old values, while preserving other entries. Stop reusing deleted content and report failed writes as not saved.

## Status and provenance

| status | Meaning | source_kind |
| --- | --- | --- |
| stated | Explicit user/source statement, not independent verification | user / document |
| uncertain | Information remains uncertain | Actual provenance |
| delegated | User delegates a particular choice/scope | user |
| draft | Provisional choice or result awaiting review | user / ai |
| declined | User declines to answer; value empty (JSON null) | user |
| user_fill | User will complete it later; value empty (JSON null) | user |
| assumed | AI assumption used to advance work | ai |
| verified | Actual verification evidence exists | verification; evidence required |

source is a short, locatable provenance reference. note can hold scope, completion location, or the effect of uncertainty. Separate linked items may capture delegation and the AI's tentative choice; do not overwrite the delegated scope with the AI's decision.

For Markdown, the AI maintains these fields directly; the JSON script checks fields and evidence-reference presence, not truth. Both modes must ground source/evidence in real conversation or results. Records do not grant execution permission.

## JSON: optional tool reads, records, and corrections

```text
python -X utf8 <skill>/scripts/feedback.py --context <stable task key> show
python -X utf8 <skill>/scripts/feedback.py --context <stable task key> show --id runtime
```

show returns current entries, never history, normally within 1600 characters. Summary fields are excerpts; use --id for details. TRUNCATED means the read was incomplete, not that no other requirements exist. Adjust `--max-chars` only for a concrete need (200–8000), avoiding repeated unrelated reads.

Example input JSON:

```json
{
  "id": "runtime",
  "question": "Which runtime is currently used?",
  "value": "Possibly Python; version uncertain",
  "status": "uncertain",
  "source_kind": "user",
  "source": "The user's runtime answer in this exchange",
  "note": "Do not select dependencies until the version is established"
}
```

```text
python -X utf8 <skill>/scripts/feedback.py --context <stable task key> record --entry <private-input.json>
```

Read the same id back after saving. Corrections submit a complete new item and a reason such as “User corrected the runtime version.” The script retains the previous item and reason. Do not write without new feedback. Record the change and check affected work rather than continuing under superseded conditions.

```text
python -X utf8 <skill>/scripts/feedback.py --context <stable task key> forget --id runtime
```

When deletion is requested, forget removes that item and its related history while retaining others. Corrupt storage is not overwritten automatically. Wait for an active writer rather than removing unknown locks. Writes use a same-directory temporary file and atomic replacement; report failed writes as not saved.
