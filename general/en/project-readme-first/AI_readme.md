# AI Navigation: project-readme-first

- Scope: This directory is one independently installable skill. Read useful project Markdown before targeted configuration or source inspection; maintain missing or outdated entry documents.
- Installation/maintenance reading: [AI_readme.md](AI_readme.md) → [README.md](README.md) → [SKILL.md](SKILL.md); read [agents/openai.yaml](agents/openai.yaml) only for interface changes.
- Routine invocation loads SKILL.md only; do not add this guide and README to every invocation.
- Layout: README.md, AI_readme.md, SKILL.md, agents/openai.yaml, and [LICENSE](LICENSE). No script dependencies, external services, or build step.
- Installation: Use a user skill directory the host actually discovers. Copy the entire skill folder, one language only; back up a same-name folder outside discovery directories. Do not copy parent levels such as general/en.
- Invariants: AI_readme.md is preferred but not the only source. Do not create documents during read-only work without authorization; mark unknown facts as unconfirmed.
- Changes: Synchronize the other language edition, usage, and interface text; do not read unrelated repository skills.
- Checks: skill-creator quick_validate, relative links, interface YAML, bilingual behavior, and git diff --check; separately check host discovery and actual usage when applying.
- For an installation request, follow README for installation and required integration, check host discovery, and briefly report the installed path and an invocation example.
- Last verified: 2026-10-02; entry documents and structure checks. Actual discovery depends on the host.
