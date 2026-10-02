# Project README First

Read useful project Markdown before targeted configuration or source inspection; maintain missing or outdated entry documents.

## Standalone installation

1. Obtain this entire skill folder. Read [AI_readme.md](AI_readme.md), this file, and [SKILL.md](SKILL.md) before installing. No other repository skill is required.
2. Copy the whole folder as `project-readme-first/` inside the host's user skill directory. Current Codex documentation uses `~/.agents/skills/`; environments using `~/.codex/skills/` or `$CODEX_HOME/skills/` should follow their actual host configuration. Avoid duplicate installations across directories.
3. Install one language only. Before replacing a same-name folder, back it up outside skill discovery directories, then replace the whole folder while preserving other skills.
4. Check that the installed `SKILL.md` is readable and the host discovers it. If absent, restart the host and invoke the skill explicitly.

Give this prompt to a Codex/GPT assistant with local file tools, replacing the download path:

```text
Install the project-readme-first skill I downloaded to <this skill folder>.
Read AI_readme.md, README.md, and SKILL.md first. Check completeness, dependencies, and the user skill directory this host actually discovers.
Install only the language edition in this folder. Back up a same-name installation outside discovery directories, then copy the entire folder; do not install both editions.
Check the installed files and host discovery. Report the path and any incomplete steps. Do not change unrelated skills or global rules.
```

A web-only chat cannot write to your computer; use an assistant with local file tools. See [official OpenAI guidance](https://learn.chatgpt.com/docs/build-skills) for host locations and discovery.

## Usage and boundaries

```text
Use $project-readme-first to understand this project, starting with useful Markdown before inspecting details.
```

AI_readme.md is preferred but not the only source. Do not create documents during read-only work without authorization; mark unknown facts as unconfirmed. Read [SKILL.md](SKILL.md) for the full workflow.

## Files and maintenance

- [README.md](README.md): human-facing installation, use, and maintenance.
- [AI_readme.md](AI_readme.md): AI installation and maintenance navigation; unnecessary for routine invocation.
- [SKILL.md](SKILL.md): trigger metadata and execution rules.
- [agents/openai.yaml](agents/openai.yaml): host interface text.
- [LICENSE](LICENSE): MIT license, retained when copying or distributing separately.

No scripts, external dependencies, or build step. Keep both language editions synchronized. Validate the entry with skill-creator's `quick_validate.py <skill-folder>`; check relative links and interface YAML. Documentation and static validation do not prove behavior inside a host; verify with usage feedback.
