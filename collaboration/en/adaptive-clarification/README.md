# Adaptive Clarification

Reuse documents and feedback before deciding whether to ask proactively. Adapt depth to engineering, learning, or creative work, retaining correctable answers, delegation, refusals, and deferred items. Respond to explicit interview requests and proceed directly when context is sufficient.

## Installation and use

Give a complete folder or ZIP to an AI with local file tools, for example:

```text
Install the skill in <this skill folder>. Read README.md and AI_readme.md first.
```

Read this file, [AI_readme.md](AI_readme.md), and [SKILL.md](SKILL.md). Confirm the host discovery directory and copy one language's entire `adaptive-clarification/`. Back up a same-name installation outside discovery directories and preserve other skills. Check discovery, entry files, and scripts, then report the installed path and invocation. No global rule changes are required. Implicit selection depends on host support and is not guaranteed every turn.

Core instructions are host-neutral; `agents/openai.yaml` is optional interface metadata. The feedback tool uses Python 3.9+ standard library with no network or external dependencies. Without files or Python, clarification still works with conversation-only summaries and disclosed persistence limits.

Ordinary task descriptions can activate it. On hosts supporting `$skill-name`, it can also be invoked explicitly:

```text
Use $adaptive-clarification to read the project context and ask only about consequential gaps.
```

## Feedback records

- Data defaults to `~/.agent-feedback/`, outside skill/repository folders. AGENT_FEEDBACK_ROOT can select a private root; isolate stable project/task contexts.
- Distinguish statements, uncertainty, delegation, drafts, refusals, user-completed fields, AI assumptions, and verification. Store provenance/evidence separately. User statements are not independent tests; scripts cannot establish truth.
- Read bounded current summaries, retain previous state/reason on corrections, and remove an item with its history on deletion requests. Records do not authorize actions.
- Never store secrets, entire chats, or unrelated personal information, and never publish records. Honor conversation-only or no-recording requests.

See [feedback records](references/feedback-records.md) for fields and commands. Installation does not invent feedback; record actual answers during use.

## Helpers and replacement

No helper skills are required. Optionally use project-readme-first for project context and user-assisted-operations for resource preparation. Share relevant feedback with adaptive-learning-guide rather than restarting intake.

This can replace explicit-only grill-me. **Only when replacement is requested**, verify/install the new skill before moving old grill-me outside discovery directories as a backup. Ordinary installation must not remove unrelated skills. Keep backups and personal records out of the public package.

## Files and maintenance

- [SKILL.md](SKILL.md): questioning, depth, and feedback rules.
- [AI_readme.md](AI_readme.md): AI installation and maintenance navigation.
- [agents/openai.yaml](agents/openai.yaml): optional interface text.
- [scripts/feedback.py](scripts/feedback.py): private revisions, bounded reads, and deletion.
- [references/feedback-records.md](references/feedback-records.md): on-demand storage guide.
- [references/behavior-checks.md](references/behavior-checks.md): maintenance scenarios.
- `tests/test_feedback.py`: unit/CLI checks; [LICENSE](LICENSE): MIT license.

No build step. Run `python -X utf8 -m unittest discover -s <skill>/tests`, skill-creator quick_validate, YAML/link checks, and scenario reviews. Keep bilingual scripts/tests identical and prose equivalent. Script tests alone do not establish conversation quality or compatibility with every host.
