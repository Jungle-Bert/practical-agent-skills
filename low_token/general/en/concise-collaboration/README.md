# Concise Collaboration

Keep replies brief and action-focused when the user requests concise communication or lower token use.

## Standalone installation

1. Obtain this entire skill folder. Read [AI_readme.md](AI_readme.md), this file, and [SKILL.md](SKILL.md) before installing. No other repository skill is required.
2. Copy the whole folder as `concise-collaboration/` inside the host's user skill directory. Current Codex documentation uses `~/.agents/skills/`; environments using `~/.codex/skills/` or `$CODEX_HOME/skills/` should follow their actual host configuration. Avoid duplicate installations across directories.
3. Install one language only. Before replacing a same-name folder, back it up outside skill discovery directories, then replace the whole folder while preserving other skills.
4. Check that the installed `SKILL.md` is readable and the host discovers it. If absent, restart the host and invoke the skill explicitly.

Give a folder path or complete skill ZIP to an AI with local file tools, for example:

```text
Install the skill in <this skill folder>. Read README.md and AI_readme.md first.
```

A web-only chat cannot write to your computer; use an assistant with local file tools. See [official OpenAI guidance](https://learn.chatgpt.com/docs/build-skills) for host locations and discovery.

## Usage and boundaries

```text
Use $concise-collaboration to briefly report the outcome, validation, and remaining issues.
```

Default to Chinese unless requested otherwise. Treat reports during ongoing tests as observations unless the user asks to investigate or fix them. Read [SKILL.md](SKILL.md) for the full workflow.

## Files and maintenance

- [README.md](README.md): human-facing installation, use, and maintenance.
- [AI_readme.md](AI_readme.md): AI installation and maintenance navigation; unnecessary for routine invocation.
- [SKILL.md](SKILL.md): trigger metadata and execution rules.
- [agents/openai.yaml](agents/openai.yaml): host interface text.
- [LICENSE](LICENSE): MIT license, retained when copying or distributing separately.

No scripts, external dependencies, or build step. Keep both language editions synchronized. Validate the entry with skill-creator's `quick_validate.py <skill-folder>`; check relative links and interface YAML. Documentation and static validation do not prove behavior inside a host; verify with usage feedback.
