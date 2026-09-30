# Low Codex Skills

English | [中文](README.md)

Personal Codex skills that reduce repetitive communication, unnecessary searches, and context reading. Skills are grouped into **general** and **hardware**, with Chinese and English editions. No fixed percentage of token savings is claimed.

## Skills

| Category | Skill | Purpose | 中文 | English |
| --- | --- | --- | --- | --- |
| General | concise-collaboration | Keep replies brief and avoid repeating context | [中文](general/zh/concise-collaboration/SKILL.md) | [English](general/en/concise-collaboration/SKILL.md) |
| General | project-readme-first | Read project Markdown before targeted source inspection | [中文](general/zh/project-readme-first/SKILL.md) | [English](general/en/project-readme-first/SKILL.md) |
| General | user-assisted-operations | Coordinate costly downloads, file preparation, and account access | [中文](general/zh/user-assisted-operations/SKILL.md) | [English](general/en/user-assisted-operations/SKILL.md) |
| Hardware | hardware-connection-check | Confirm debugger and peripheral connections before targeted checks | [中文](hardware/zh/hardware-connection-check/SKILL.md) | [English](hardware/en/hardware-connection-check/SKILL.md) |

```text
general/
  zh/<skill-name>/SKILL.md
  en/<skill-name>/SKILL.md
hardware/
  zh/hardware-connection-check/SKILL.md
  en/hardware-connection-check/SKILL.md
```

Each skill also includes `agents/openai.yaml` with interface text in the corresponding language.

## Installation and use

Copy the **entire skill folder** in your chosen language into `$CODEX_HOME/skills/`, or `~/.codex/skills/` when `CODEX_HOME` is unset. For example, copy `general/en/project-readme-first/` to `~/.codex/skills/project-readme-first/`.

Both editions use the same skill name. Install one language per skill to avoid name conflicts. Check and back up any existing skill before replacing it; replace the whole corresponding folder when switching editions. Invoke a skill with `$project-readme-first`, `$concise-collaboration`, and so on, or let Codex select it when relevant.

The English editions translate the instructions and preserve their behavior. `concise-collaboration` still defaults to Chinese replies unless the user requests another language.

## Source and maintenance

The three general skills come from the author's existing local skills. `hardware-connection-check` was extracted from the local-device collaboration guidance in `user-assisted-operations`, with the author's requested ordering: ask about connections before searching for devices. The general edition no longer handles device connection checks.

This repository contains skill documentation and needs no build, deployment, or environment variables. Keep both language editions, the index, and interface metadata in sync. See [AI_readme.md](AI_readme.md) for maintenance and validation guidance.

## License

Released under the [MIT License](LICENSE), allowing use, modification, and redistribution.
