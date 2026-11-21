# Private feedback records

Load only for task feedback reads or writes. Python 3.9+ standard library only. Without execution support, maintain equivalent fields in the conversation and disclose that they are not persisted.

## Location and scope

Default root: `~/.agent-feedback/`. AGENT_FEEDBACK_ROOT or the leading `--root <private directory>` option can override it. The script rejects repository/skill storage and context paths escaping the root.

Choose a stable context, such as `project:<canonical project root>`; append a fixed task key for independent tasks within a project. Keep it when wording or answers change and include it in handoff summaries. Separate projects and users; use a separate scope for global preferences only when explicitly established. Do not scan other contexts by default.

Each context has `contexts/<context-hash>/feedback.json` with current items and short revision history. This is plaintext local summary storage, not a secret vault. Never store secrets, whole chats, or unrelated personal data. Prepare input JSON in private working storage, not the public repository.

## Status and provenance

| status | Meaning | source_kind |
| --- | --- | --- |
| stated | Explicit user/source statement, not independent verification | user / document |
| uncertain | Information remains uncertain | Actual provenance |
| delegated | User delegates a particular choice/scope | user |
| draft | Provisional choice or result awaiting review | user / ai |
| declined | User declines to answer; value must be null | user |
| user_fill | User will complete it later; value must be null | user |
| assumed | AI assumption used to advance work | ai |
| verified | Actual verification evidence exists | verification; evidence required |

source is a short, locatable provenance reference. note can hold scope, completion location, or the effect of uncertainty. Separate linked items may capture delegation and the AI's tentative choice; do not overwrite the delegated scope with the AI's decision.

The script checks fields and evidence-reference presence, not truth. The executing AI must ground source/evidence in real conversation or results. Records do not grant execution permission.

## Read, record, and correct

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
