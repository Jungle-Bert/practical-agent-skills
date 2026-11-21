# AI Navigation: adaptive-clarification

- Scope: Proactive clarification and feedback across tasks, including explicit interview requests; proceed when context suffices.
- Installation/maintenance: this guide → [README.md](README.md) → [SKILL.md](SKILL.md). Routine use loads SKILL.md; read [references/feedback-records.md](references/feedback-records.md) only for storage operations.
- Installation: Copy one complete language edition to a discovered host location and back up same-name installs outside discovery directories. Check entries, scripts, and discovery; report invocation. No global rules required. Back up/disable old grill-me only when replacement is requested.
- Layout: README, AI_readme, SKILL, [agents/openai.yaml](agents/openai.yaml), [LICENSE](LICENSE), plus scripts/, references/, and tests/. Interface YAML is optional; persistence uses Python 3.9+ standard library, without network dependencies.
- [scripts/feedback.py](scripts/feedback.py): Read current feedback, revise, and delete by stable context. Private data defaults to ~/.agent-feedback; AGENT_FEEDBACK_ROOT can override it. Repository/skill storage is rejected.
- Invariants: Reuse before asking; distinguish uncertainty, delegation, drafts, refusal, manual completion, and verification; silence is not agreement and records grant no authority. Store necessary real information only, never publish personal records.
- Changes: Keep scripts and tests/test_feedback.py identical across languages, prose equivalent, and docs/UI synchronized. Keep personal materials and backups outside the skill.
- [references/behavior-checks.md](references/behavior-checks.md): Maintenance review of proactive questioning, sufficient sources, corrections, and topic depth; not routine context.
- Checks: quick_validate, python -X utf8 -m unittest discover -s <skill>/tests, YAML, relative links, bilingual layout, and git diff --check. Distinguish script tests, maintainer walkthroughs, and real conversation quality.
- Last verified: 2026-11-21; script/CLI tests, entry, YAML, links, and maintainer scenario review. Ongoing conversations and other-host discovery need usage validation.
