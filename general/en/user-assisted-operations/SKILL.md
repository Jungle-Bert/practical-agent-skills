---
name: user-assisted-operations
description: Identify downloads, uploads, copying, file preparation, account access, and asset collection that the user can complete more quickly or reliably than Codex. Finish independent work first, then request a specific manual action with a destination and verification method. Applies to development, files, resource access, and local collaboration, not inexpensive routine operations Codex can safely complete.
---

# User-Assisted Operations

Compare the total cost of Codex execution and manual user action. Give the user a small number of clear, easy actions while continuing all work that does not depend on them.

## When to request assistance

For downloads, copying, uploads, exports, drag-and-drop, login, authorization, private materials, or large resource preparation, consider:

- Whether the user can complete the action in a few steps while Codex would need lengthy searches, transfers, repeated retries, or reconstruction.
- Whether the action depends on the user's account, browser session, local path, private files, paid resources, or explicit authorization.
- Whether self-execution has significant token, network, compute, or retry costs.
- Whether original resources supplied manually would be more accurate than imitation, another download, or reconstruction.

Prepare an assistance request when one of these is clearly true. Do not delegate inexpensive, safe file operations, simple searches, or small conversions without a reason.

## Workflow

1. Separate independent work from work that depends on an external action.
2. Complete all independent analysis, code, documentation, directory preparation, and verification first.
3. Request the useful manual action at a progress checkpoint or after the current stage. Do not stop early when substantial independent work remains.
4. Make the request executable: state the action, source or location, destination filename or format, delivery method, and completion signal.
5. Give feasible options. Prefer the efficient manual action; if the user wants Codex to try, explain the cost or permissions. Where useful, state how work can continue without the resource.
6. After the user acts, verify existence, format, and readability before continuing dependent work.
7. Do not repeatedly prompt an inactive user. Continue through an inexpensive alternative if one exists; otherwise state the blocker and missing resource.

## Request contents

Keep each request to one closely related set of actions, including:

- **Completed:** briefly state what is ready.
- **Action:** give a specific step or a few steps.
- **Destination or delivery:** specify the filename, location, upload method, or response format.
- **Reason:** explain the avoided lengthy download, rebuild, or token cost.
- **Completion signal:** say whether to reply that it is done, upload the file, or provide a path.
- **Fallback:** explain the cost of Codex execution or why dependent work cannot continue yet.

Example:

> A and B are ready. For C, manual preparation is quicker: obtain the resource from [source], name it [filename], and place it in [destination]. Reply when it is ready; I will verify it and continue D. If you prefer that I try, it may add [time, download, or permission cost].

## Common cases

- **Known download:** when the user can directly access a specific link, suggest downloading to a specific location. Avoid lengthy scraping, unpacking, or rebuilding for an existing resource.
- **Large or private files:** ask the user to copy from their local source into the specified project location or supply it through an available upload method. Do not guess local paths.
- **Accounts and access:** ask the user to log in or authorize in their browser or app, then continue. Never request passwords, tokens, or private keys.
- **User-owned assets:** prefer original images, templates, data, exports, or screenshots over imitation that loses quality or accuracy.
- **Desktop actions:** when the user must click, select a directory, or confirm a system dialog, give precise steps and subsequent verification. Device connection confirmation belongs to the separate hardware-connection-check skill.
- **Costly builds or repeated generation:** prefer reusable build outputs, dependencies, templates, or samples the user already has instead of recreating them.

## Boundaries

- When the user explicitly asks Codex to complete the work, do not switch to manual execution unless permissions, resources, or safety limitations prevent it.
- Do not transfer coding, debugging, or ordinary inexpensive commands merely because they seem inconvenient.
- Do not request passwords, private keys, access tokens, or other secrets. Use login, authorization, upload, or redacted-file workflows.
- Do not assume permission for risk, spending, or external publication. Explain the impact and obtain confirmation when existing authorization does not cover it.
- Assistance requests do not replace progress reports. Deliver what is ready, then describe dependencies, recommended actions, and next steps.
