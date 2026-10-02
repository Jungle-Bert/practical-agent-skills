# AI Navigation

- Scope: Compact metadata retrieval and on-demand cards; personal data is outside the public skill.
- Normal use loads only [SKILL.md](SKILL.md) and executes the script; do not load this guide, README, source, or all index.jsonl. For maintenance/development, read this guide and [README.md](README.md) first.
- Read [references/maintenance.md](references/maintenance.md) and the template only when writing.
- scripts/pitfalls.py: search reads metadata only; get verifies the selected card hash; index updates one record and preserves others.
- Dependencies: Python 3.9+ standard library, no network service. Python/PyYAML are needed only for frontmatter validation.
- Checks: unittest discovery under tests, skill-creator quick_validate, and git diff --check. Both language editions must have identical scripts.
- Invariants: Search never reads cards; normal knowledge output ≤3000 characters; no-match never scans details; preserve evidence boundaries; no personal data/absolute paths in the public repo.
- Synchronize language docs and templates after schema changes. No build/deployment; publication uses Git commit/push.
- Last verified: 2026-10-02; structure and script tests. Invocation depends on host loading.
