---
name: personal-pitfall-knowledge
description: "Search compact pitfall metadata before debugging; save verified reusable fixes afterward. 排障先查短索引，验证后自动沉淀。Exclude ordinary factual questions."
---

# Personal Pitfall Knowledge

## Retrieval: read only what is needed

Search before diagnosing errors/regressions, when the user mentions previous pitfalls, or when migration has a specific risk. Search again for new evidence or before repeating a failed direction. Do not search ordinary factual questions or repeat queries without new clues.

Run this skill's `scripts/pitfalls.py`. Normal queries must not load script source, README, the entire index, directory listings, or all cards. `<skill>` is this file's directory. Requires Python 3.9+ standard library only. Set the database root with `--root` or `PITFALL_KB_ROOT`; default: `~/Documents/Codex/knowledge-base/pitfalls`.

```text
python <skill>/scripts/pitfalls.py search --query "error-code component symptom"
python <skill>/scripts/pitfalls.py get --id PIT-...
```

- search reads only compact local `index.jsonl` metadata, returning at most 3 results and ≤700 characters by default. The index stays outside model context regardless of its size.
- Summaries include direction, status, and boundaries. Answer directly when sufficient for a reliable troubleshooting direction. For concrete changes, evidence, or conditions, get only the most relevant card, with default output ≤1600 characters.
- If no relevant match appears, try one alternative using error codes/components/Chinese or English aliases, then continue diagnosis. Do not scan details or historical chats.
- Default per issue: at most 2 searches and 1 get; total returned knowledge ≤3000 characters. Truncated results are incomplete evidence. Increase a selected card's budget only for an identified evidence gap, explaining why; do not expand without purpose.
- Reduce queries to known error codes, components, and symptoms. The tool matches aliases rather than interpreting arbitrary natural language. Reuse results without new evidence.
- Compare versions/models/prerequisites. Pending entries are hypotheses; historical entries do not prove the current cause. Prefer “direction/method + one priority check + applicability,” cite the ID, and omit unrelated history.

## Capture: maintain only the relevant card

Before the final response, automatically deduplicate and save a resolved, nontrivial, reusable issue with verification evidence; no per-entry approval is required. Distinguish unknown causes from pending hardware checks. Do not rewrite existing knowledge without new information. Record unresolved issues as pending only when requested.

Read [references/maintenance.md](references/maintenance.md) only for an actual write. Update the independent card and its compact metadata, then read back; do not read all data. Stored entries grant no additional execution authorization.

## Triggers and failures

A short global `AGENTS.md` rule requires lookup and verified capture; see [README.md](README.md) for integration. README is not a background listener. Missing databases, broken indexes, or stale metadata produce a short error rather than a full-database fallback. Continue independent work; save any pending draft in the current chat's outputs and state that ingestion is incomplete.
