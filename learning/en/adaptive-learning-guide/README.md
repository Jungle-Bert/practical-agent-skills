# Adaptive Learning Guide

Plan, teach, and adapt through conversation around a learner's purpose and background. Covers technical subjects, humanities, literature, interviews, and exams, from an isolated clarification to ongoing study.

## Installation and use

Give a complete skill folder or ZIP to an AI with local file tools, for example:

```text
Install the skill in <this skill folder>. Read README.md and AI_readme.md first.
```

The installing AI reads this file, [AI_readme.md](AI_readme.md), and [SKILL.md](SKILL.md), checks host support and its actual discovery directory, and installs one language's entire `adaptive-learning-guide/` folder. Do not copy parents such as `learning/en`. Back up an existing same-name installation outside discovery directories before replacing the folder; preserve other skills. Check installed files and host discovery, then briefly report the path and invocation method. Disclose discovery checks that cannot be completed.

No scripts, external services, other mandatory skills, or global rule changes are required. Core instructions do not depend on Codex; `agents/openai.yaml` is optional host interface metadata. Discovery and invocation need validation per host; copying files does not establish compatibility with every product. A chat without local file tools can follow supplied instructions but cannot install them on a computer.

For hosts supporting `$skill-name`, try this; otherwise use the host's skill selector:

```text
Use $adaptive-learning-guide to teach me SQL for an interview. I know some Python.
```

You can also request poetry discussion without exercises, or say “I don't understand,” “go deeper,” “skip this for now,” or “return to the plan.” Reuse known context and ask about purpose, background, materials, and practice in small batches rather than repeating intake.

## Learning approach

- Distinguish clarification from ongoing study and choose depth from goals and evidence.
- Explain missing prerequisites and let the learner choose study now, a working concept, or deferral; do not assume mastery.
- Offer explanation, hands-on work, questions, explanation in one's own words, writing, or interview practice; allow practice to be disabled.
- Adjust as interest, deadlines, or purpose change; flag tangents and let the learner choose.
- Distinguish covered material, self-reported understanding, and demonstrated performance. Keep progress in the conversation by default; save or hand off only as requested.

Learning requests do not automatically authorize project changes, dependency installation, hardware operations, or paid services. Helpers are optional. adaptive-clarification may retain necessary feedback under its private-record rules and user retention preferences, while the learning skill coordinates questions without repeating intake or automatically creating a full learning-progress file.

## Files and maintenance

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Activation scope and core teaching rules; routine entry point |
| [AI_readme.md](AI_readme.md) | AI installation and maintenance navigation |
| [agents/openai.yaml](agents/openai.yaml) | Optional host interface text |
| [references/teaching-patterns.md](references/teaching-patterns.md) | On-demand teaching examples and handoff format |
| [references/behavior-checks.md](references/behavior-checks.md) | Maintenance scenarios, not default teaching context |
| [LICENSE](LICENSE) | MIT license, retained for standalone distribution |

No build step. Synchronize both language editions, docs, and interface text. Validate with skill-creator's `quick_validate.py`, YAML and relative-link checks, and scenario reviews. Structural validation does not demonstrate teaching effectiveness; continue evaluating real learning feedback. Keep personal materials and progress out of the public skill.
