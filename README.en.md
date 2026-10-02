# Low Codex Skills

English | [中文](README.md)

Personal Codex skills that reduce repetitive communication, unnecessary searches, and context reading. Skills are grouped into **general** and **hardware**, with Chinese and English editions. No fixed percentage of token savings is claimed.

## Skills

| Category | Skill | Purpose | 中文 | English |
| --- | --- | --- | --- | --- |
| General | concise-collaboration | Keep replies brief and avoid repeating context | [中文](general/zh/concise-collaboration/README.md) | [English](general/en/concise-collaboration/README.md) |
| General | project-readme-first | Read project Markdown before targeted source inspection | [中文](general/zh/project-readme-first/README.md) | [English](general/en/project-readme-first/README.md) |
| General | user-assisted-operations | Coordinate costly downloads, file preparation, and account access | [中文](general/zh/user-assisted-operations/README.md) | [English](general/en/user-assisted-operations/README.md) |
| General | personal-pitfall-knowledge | Search compact metadata, read selected cards, and save verified fixes | [中文](general/zh/personal-pitfall-knowledge/README.md) | [English](general/en/personal-pitfall-knowledge/README.md) |
| Hardware | hardware-connection-check | Confirm debugger and peripheral connections before targeted checks | [中文](hardware/zh/hardware-connection-check/README.md) | [English](hardware/en/hardware-connection-check/README.md) |

```text
general/
  zh/<skill-name>/SKILL.md
  en/<skill-name>/SKILL.md
hardware/
  zh/hardware-connection-check/SKILL.md
  en/hardware-connection-check/SKILL.md
```

Each skill has the same base layout and can be installed by copying its folder alone:

```text
<skill-name>/
  README.md                 Human installation, usage, and maintenance
  AI_readme.md              AI installation and maintenance navigation
  SKILL.md                  Trigger metadata and execution rules
  agents/openai.yaml        Interface text
  LICENSE                   MIT license
  scripts/                  Optional executable tools
  references/               Optional maintenance guidance and templates
  tests/                    Optional tool tests
```

Only `personal-pitfall-knowledge` currently needs the last three directories. Other skills have no empty placeholder directories. Routine invocation reads `SKILL.md` and task-relevant resources; installation and maintenance use the README and AI guide.

## Installation and use

Install manually or give a prompt below to a Codex/GPT assistant with local file and download tools. A web-only chat cannot install directly on your computer.

### Determine the installation directory

Current [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) recommends `~/.agents/skills/` for user skills and `.agents/skills/` for project skills. Existing environments may still load from `~/.codex/skills/` or `$CODEX_HOME/skills/`; follow the actual host configuration or skill list. Do not install duplicate names across discovery directories. Here, `<skills-dir>` means the confirmed user skill directory.

Read each selected skill's `AI_readme.md`, `README.md`, and `SKILL.md` first. Install one language per skill. Back up a same-name installation outside discovery directories before replacing the whole folder; preserve unrelated skills. Check installed files and host discovery. Restart the host if needed; a successful copy alone does not demonstrate invocation.

### Method one: Install all skills

1. [Download and extract the repository ZIP](https://github.com/Jungle-Bert/low_codex_skills/archive/refs/heads/main.zip), or run `git clone https://github.com/Jungle-Bert/low_codex_skills.git`.
2. Choose `en` or `zh`. Copy the four skill folders under `general/<language>/` and the one under `hardware/<language>/` separately into `<skills-dir>/`.
3. Each target is `<skills-dir>/<skill-name>/SKILL.md`: five skills total. Do not copy category/language parents or install all ten bilingual editions.
4. `personal-pitfall-knowledge` needs Python 3.9+. For automatic troubleshooting lookup and capture, follow its README to integrate global rules. Store personal data outside the skill folder.

**Prompt for a local assistant:**

```text
Install all English skills from https://github.com/Jungle-Bert/low_codex_skills.
Clone or download the ZIP, or reuse an existing complete local copy. Read repository AI_readme.md and README.en.md,
then AI_readme.md, README.md, and SKILL.md for each skill under general/en/ and hardware/en/.
Confirm the user skill directory this host actually discovers. Install only these five skills:
concise-collaboration, project-readme-first, user-assisted-operations,
personal-pitfall-knowledge, and hardware-connection-check.
Back up same-name installations outside discovery directories, then copy each entire folder;
preserve unrelated skills and do not install the Chinese editions.
Check Python 3.9+. Follow the pitfall README to merge trigger rules into the global AGENTS.md the host actually loads,
preserving existing rules and personal data rather than replacing the file. If no database exists,
report the initialization requirement instead of claiming lookup is ready.
Verify installed files and host discovery. Report skill paths, backup locations, and incomplete steps.
```

For Chinese editions, replace English/en with Chinese/zh. The English concise skill still defaults to Chinese replies unless another language is requested. For an existing download, change the first sentence to “Install all English skills from the repository extracted at <repository folder>”; no new download is needed.

### Method two: Install one skill

1. Download/clone the repository and use only the desired folder, such as `general/en/project-readme-first/`. A local assistant may instead retrieve that complete folder alone.
2. Read its `AI_readme.md` and `README.md`; copy the entire folder as `<skills-dir>/project-readme-first/`, retaining `agents/`, `LICENSE`, and its actual resources.
3. Invoke `$project-readme-first`, or let Codex select it for relevant tasks. No other skill is required; follow the selected skill's README for extra integration such as global rules.

**Prompt for a local assistant:**

```text
Install only the English project-readme-first skill from
https://github.com/Jungle-Bert/low_codex_skills/tree/main/general/en/project-readme-first.
You may clone or download the repository, but install only this skill.
Read its AI_readme.md, README.md, and SKILL.md first; confirm completeness and the user skill directory this host discovers.
Back up a same-name installation outside discovery directories, then copy the entire folder, retaining LICENSE.
Do not install other skills or the Chinese edition, or change unrelated global rules.
Verify installed files and host discovery. Report the path, backup, and incomplete steps.
```

Replace the URL, name, and language for another skill. If you have a downloaded standalone folder, use the offline prompt in its README.

## Contributions and repository permissions

A public repository can be viewed, downloaded, and forked by anyone. Direct pushes require the owner or a collaborator with write access and remain subject to branch rules; public visibility does not grant write access. See [GitHub permissions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository).

Others can fork and open a pull request for maintainer review. Keep both language editions, documentation, and interface metadata synchronized, complete validation, and exclude personal data and credentials.

## Source and maintenance

This project is the permanent maintenance home for personal skills. Codex writes, updates, applies, and validates skills, then uploads the user-selected scope to this repository's GitHub remote. Repository sources and locally installed copies are maintained separately. Publish only selected skills and their necessary supporting files. See [AGENTS.md](AGENTS.md) for project agreements.

The three general skills come from the author's existing local skills. `hardware-connection-check` was extracted from the local-device collaboration guidance in `user-assisted-operations`, with the author's requested ordering: ask about connections before searching for devices. The general edition no longer handles device connection checks.

The pitfall search tool requires Python 3.9+ standard library. Optional PITFALL_KB_ROOT selects the local database; the default is a fixed location under the user's Documents directory. Normal queries return only short results rather than all knowledge. See its [README](general/en/personal-pitfall-knowledge/README.md) for budgets, triggers, and usage. Personal entries are not published with the skill.

No build or deployment is needed. Keep both language editions, the index, and interface metadata in sync. See [AI_readme.md](AI_readme.md) for maintenance and validation guidance.

## License

Released under the [MIT License](LICENSE), allowing use, modification, and redistribution.
