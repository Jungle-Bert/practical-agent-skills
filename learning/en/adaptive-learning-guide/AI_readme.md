# AI Navigation: adaptive-learning-guide

- Scope: Standalone conversational learning guidance adapting to purpose, background, prerequisites, and feedback; core instructions are host-neutral.
- Installation/maintenance reading: this guide → [README.md](README.md) → [SKILL.md](SKILL.md). Routine teaching loads SKILL.md and relevant examples only.
- Installation: Confirm host support and discovery directory, copy one language's complete folder, back up same-name installs outside discovery directories, and preserve other skills. Check discovery and report path and invocation. No global rule integration is needed.
- Layout: README.md, AI_readme.md, SKILL.md, [agents/openai.yaml](agents/openai.yaml), [LICENSE](LICENSE), and references/. No scripts, mandatory dependencies, or build step. Interface YAML is not a universal host requirement.
- [references/teaching-patterns.md](references/teaching-patterns.md): Purpose, prerequisite, and handoff examples; read only for the relevant situation.
- [references/behavior-checks.md](references/behavior-checks.md): Maintenance scenarios for evaluating actual responses, not routine teaching context. Do not replace behavioral evaluation with string matching.
- Invariants: Do not force courses on isolated questions; let users choose prerequisite depth; support learning without exercises; preserve task goals; distinguish exposure from mastery; never invent cross-chat memory.
- Data and helpers: Keep personal materials and progress out of the public skill; save files as requested. Helpers are optional and follow their own activation conditions; teaching works without them.
- Clarification: Optionally reuse task feedback through adaptive-clarification; the learning skill coordinates teaching questions without repeating intake.
- Changes: Synchronize the other edition and README. Edit agents/openai.yaml only for interface changes. Distinguish static checks, scenario walkthroughs, and real tutoring evidence.
- Checks: skill-creator quick_validate, interface YAML, relative links, git diff --check, and scenario walkthroughs as needed. Static checks alone cannot establish teaching quality or cross-host discovery.
- Last verified: 2026-11-21; optional clarification coordination updated; entry, interface YAML, links, and maintenance scenario walkthrough. Long-term tutoring and other-host compatibility need usage validation.
