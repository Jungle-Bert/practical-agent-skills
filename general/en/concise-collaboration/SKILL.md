---
name: concise-collaboration
description: Keep conversation replies concise, action-focused, and low-redundancy when the user asks for brief answers, reduced token usage, or a concise communication mode.
---

# Concise Collaboration

Use this mode for the current reply and task unless correctness, safety, or the user's requested detail requires more explanation.

- Use Chinese by default; follow an explicit request for another language.
- Lead with the conclusion.
- Keep simple answers to roughly 3–5 lines.
- Do not repeat known background, full plans, or tool output.
- After code changes, report only changes, verification, and remaining issues.
- Explain underlying principles only when requested.
- Avoid alternatives unless there is a real tradeoff or risk.
- Keep progress updates short and send them only for meaningful progress, blockers, or long-running operations.

## Test Observation Mode

When the user reports a problem while hardware, firmware, or PC software testing is still running:

- Treat the report as an observation to record, not an immediate change request.
- Do not modify code, build, flash, restart, disconnect, or otherwise interrupt the test.
- Give a brief acknowledgment and, when useful, a tentative cause to observe.
- Wait until the user says the test is complete or explicitly asks to investigate or fix it before acting.
- If there is a credible risk of hardware damage or unsafe operation, warn the user immediately.

Explicit modes:

- `conclusion only`: give the conclusion and essential evidence only.
- `concise analysis`: give the judgment and the smallest useful reasoning.
- `concise execution`: make the requested change and give a compact result.
- `detailed explanation`: temporarily provide a fuller explanation.
