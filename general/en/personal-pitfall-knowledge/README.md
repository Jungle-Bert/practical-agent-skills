# Personal Pitfalls: Small-Context Retrieval

## Purpose and layout

Search short metadata for a troubleshooting direction, then read one card only when needed. Do not load the full database/index or script source by default. Only bounded results enter model context. Savings concern context content, not a guaranteed token percentage; character limits are not exact tokenizer counts.

```text
<knowledge-root>/
  index.jsonl             Short summaries and aliases, searched locally
  entries/PIT-....md       Independent detailed cards
  archive/                Historical snapshots, excluded from queries
```

The skill includes a short SKILL.md, scripts/pitfalls.py, write-only references, UI YAML, and AI navigation. Install one language into `$CODEX_HOME/skills/personal-pitfall-knowledge`, defaulting to `~/.codex/skills/`.

## Triggers and integration

Add these short rules to global `~/.codex/AGENTS.md`, using the actual installed skill path:

```text
For errors/regressions, previous pitfalls, or identified migration risks, load installed personal-pitfall-knowledge/SKILL.md and search compact metadata first.
Search new clues when evidence changes or a failed direction may be repeated; do not search ordinary questions or repeat unchanged queries.
For resolved reusable issues with verification, deduplicate, automatically update the card and metadata, and read back; no per-entry approval.
Return at most 3 short results and get 1 card only when needed, normally totaling ≤3000 knowledge characters; never traverse the full database into context.
```

README explains, SKILL executes, and global instructions require invocation; there is no background listener. Explicit `$personal-pitfall-knowledge` also works. Triggers depend on global instructions being loaded and paths remaining accessible.

## Usage and budget

Python 3.9+ standard library only. Configure the database with `--root` or `PITFALL_KB_ROOT`; default: `Documents/Codex/knowledge-base/pitfalls` inside the user's home directory.

```text
python <skill>/scripts/pitfalls.py --root <knowledge-root> search --query "C1041 PDB"
python <skill>/scripts/pitfalls.py --root <knowledge-root> get --id PIT-...
```

Each search returns ≤700 characters and at most 3 matches; get defaults to ≤1600. Normal flow is one search with zero or one card read; at most one alternate query, totaling ≤3000 characters. Increase `--max-chars` only for an identified gap. Budgets include returned knowledge text, not tool-call/skill-loading overhead or the conversation; reuse results without new clues.

When a summary suffices, give an accurate direction and one priority check. If ambiguous, verify the selected card's environment and state; do not claim hardware success from pending evidence. NO_MATCH does not trigger scanning; STALE_INDEX requires repairing the affected metadata before reuse.

## Capture and verification

Read [references/maintenance.md](references/maintenance.md) only for an actual write. Save the card, run `index --metadata <metadata.json>` to update metadata/hash, and get it back. Updates use locking and atomic replacement; personal data is not uploaded.

Validate structure with skill-creator quick_validate.py. Run `python -m unittest discover -s <skill>/tests` for ranking, no-detail searches, budgets, stale metadata, and preservation of other records. The database is the user's local data; this repository contains no author's knowledge records, personal absolute paths, or credentials.
