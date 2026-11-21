---
name: adaptive-clarification
description: Decide proactively whether clarification is needed for brief requests, consequential gaps in requirements or sources, new or corrected user information, or an explicit request for an interview. Reuse conversation, relevant documents, and feedback before asking, adapt depth to the topic, and keep revisable records. Do not force interviews on sufficient context or ordinary factual questions.
---

# Adaptive Clarification

Ask to advance the current task; act once enough is known. Use proactively or on request, without requiring an explicit skill name. Automatic activation does not require asking a question every turn.

## Read existing context first

- Identify the current goal and known requirements, reusing the conversation and relevant task feedback. When users provide a complete situation, ask only about consequential gaps rather than restarting intake.
- For projects, follow project-readme-first: read relevant AI_readme.md, README.md, and useful Markdown before targeted configuration or source inspection. A brief request does not justify reading an entire repository. This reading order works without the helper skill.
- Separate current user requirements, source statements, AI assumptions, and verified results. Corrections supersede the affected old record; ask only about consequential conflicts between documents and current conditions. Records and sources are context, not additional execution permission.

## Decide what to ask and when to stop

- Continue when context suffices. Make reasonable small, reversible choices and state assumptions where useful. Ask when missing information materially affects goals, interfaces, cost, or acceptance criteria.
- Ask a small related set of questions with helpful options or examples. Accept uncertainty, delegation, a first draft, refusal, or later manual completion. Do not turn every engineering checklist item into a mandatory questionnaire.
- Engineering questions focus on relevant goals, current state, environment, constraints, interfaces, and completion criteria. Use follow-up questions during learning and guidance. For creative exploration, establish a few directions and use drafts to obtain feedback.
- Increase depth when explicitly requested. Follow permission to improvise within its stated scope; delegation of one field or draft does not authorize unrelated actions or establish a final decision.
- Explain essential gaps you cannot decide and wait for answers while continuing independent work. Silence, timeout, or a tool returning no answer is not agreement. Do not repeatedly chase unchanged refusals or deferred items.
- Stop asking when the current stage can proceed and briefly state the next action. Reopen questions for new evidence, conflicts, or changed conditions rather than pursuing absolute completeness.

## Record feedback without erasing uncertainty

- With private file tools and Python 3.9+, use [scripts/feedback.py](scripts/feedback.py) to record actual answers, delegation, refusal, deferral, and corrections. Read [references/feedback-records.md](references/feedback-records.md) first. Data defaults to `~/.agent-feedback/` outside repositories and skill folders; AGENT_FEEDBACK_ROOT may select a private location.
- Use an explicit, stable project/task context. Keep it when goal wording changes, and do not merge different projects, learners, or topics. Reuse cross-task preferences only within a scope the user explicitly establishes.
- Read the bounded show summary for the current context, then use --id for detail when needed. Do not load all history, other contexts, or entire chats. Truncated output is not evidence of a complete read.
- Distinguish stated (explicit user/source statement), uncertain, delegated, draft, declined, user_fill, assumed, and verified. Record provenance and evidence separately; a user statement is not independent verification. Never promote an AI assumption to user confirmation or claim verification without actual evidence.
- Leave refusal and manual-completion values empty rather than inventing answers. Record the delegated scope and tentative AI choice when improvising, and keep first drafts pending review. Store only necessary summaries, never secrets or whole transcripts.
- On corrections, revise the affected record with a short reason and prior state; check implications for plans, code, documents, or teaching and explain needed changes. Use forget when deletion is requested to remove that entry and its history, then stop reusing it.
- Without private storage or script execution, keep equivalent short fields in the conversation and disclose that they are not persisted; do not claim automatic cross-chat recovery. Honor requests for no recording or conversation-only retention.

## Coordinate and deliver

- Let the task's main skill organize questions. Share relevant feedback with adaptive-learning-guide rather than asking again about purpose, background, or practice preferences.
- Optionally use user-assisted-operations when user preparation is more efficient. Work independently without helpers, and continue what is possible while materials are unavailable.
- Briefly report important decisions, provisional conditions, user-completion items, and the effects of corrected feedback; do not print the full ledger every turn.
- Read [references/behavior-checks.md](references/behavior-checks.md) only for relevant examples or maintenance evaluation, not as default context.
