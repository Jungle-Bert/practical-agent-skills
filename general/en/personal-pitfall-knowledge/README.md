# Personal Pitfalls: Small-Context Retrieval

## Purpose and layout

Search short metadata for a troubleshooting direction, then read one card only when needed. Do not load the full database/index or script source by default. Only bounded results enter model context. Savings concern context content, not a guaranteed token percentage; character limits are not exact tokenizer counts.

```text
<knowledge-root>/
  index.jsonl             Short summaries and aliases, searched locally
  entries/PIT-....md       Independent detailed cards
  archive/                Historical snapshots, excluded from queries
```

The folder contains the common entry documents and the resources needed for lookup and capture. Install it alone; no other repository skill is required.

## Standalone installation

1. Obtain the whole folder. Read [AI_readme.md](AI_readme.md), this file, and [SKILL.md](SKILL.md); check Python 3.9+. There are no third-party runtime dependencies.
2. Copy it as `personal-pitfall-knowledge/` under the host's user skill directory. Current [official documentation](https://learn.chatgpt.com/docs/build-skills) uses `~/.agents/skills/`; follow the actual host configuration for environments using `~/.codex/skills/` or `$CODEX_HOME/skills/`. Avoid duplicate installations.
3. Install one language. Back up same-name installations outside discovery directories before replacing the entire skill folder. Keep the personal database in its separate root; installation and updates must not overwrite it.
4. Check installed files and host discovery; restart the host if necessary. Follow the next section for automatic triggers. Copying files alone does not establish trigger integration.

Give this prompt to a Codex/GPT assistant with local file tools; a web-only chat cannot write to your computer:

```text
Install the personal-pitfall-knowledge skill I downloaded to <this skill folder>.
Read AI_readme.md, README.md, and SKILL.md first. Check Python 3.9+ and the user skill directory this host actually discovers.
Install this language only. Back up same-name installations outside discovery directories, then copy the whole folder, retaining LICENSE.
Follow the README to merge trigger rules into the global AGENTS.md the host actually loads; preserve existing rules rather than replacing the file.
Preserve personal data. If no database exists, report the initialization requirement instead of claiming lookup is ready; do not traverse personal history.
Check files, host discovery, and global integration. Report paths, backups, and incomplete steps.
```

## Skill files and maintenance

- [README.md](README.md): human installation, use, and maintenance.
- [AI_readme.md](AI_readme.md): AI installation and maintenance navigation; unnecessary for routine queries.
- [SKILL.md](SKILL.md): triggers and execution rules.
- [agents/openai.yaml](agents/openai.yaml): interface text.
- [LICENSE](LICENSE): MIT license, retained for standalone distribution.
- `scripts/`: lookup and metadata tools; `references/`: on-demand capture guidance and templates; `tests/`: script unit tests.

No build step. Synchronize both language editions; scripts must be identical. Check relative links, interface text, and the validation described below.

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
