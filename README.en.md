# Practical Agent Skills

English | [中文](README.md)

Practical skills for AI assistants covering **reduced unnecessary usage** and **guided learning**. Usage-reduction skills currently live in `low_token/general/` and `low_token/hardware/`; learning skills live in `learning/`. Each has Chinese and English editions. No fixed token or quota savings are claimed, and host compatibility requires actual validation.

## Skills

| Category | Skill | Purpose | 中文 | English |
| --- | --- | --- | --- | --- |
| Low token / General | concise-collaboration | Keep replies brief and avoid repeating context | [中文](low_token/general/zh/concise-collaboration/README.md) | [English](low_token/general/en/concise-collaboration/README.md) |
| Low token / General | project-readme-first | Read project Markdown before targeted source inspection | [中文](low_token/general/zh/project-readme-first/README.md) | [English](low_token/general/en/project-readme-first/README.md) |
| Low token / General | user-assisted-operations | Coordinate costly downloads, file preparation, and account access | [中文](low_token/general/zh/user-assisted-operations/README.md) | [English](low_token/general/en/user-assisted-operations/README.md) |
| Low token / General | personal-pitfall-knowledge | Search compact metadata, read selected cards, and save verified fixes | [中文](low_token/general/zh/personal-pitfall-knowledge/README.md) | [English](low_token/general/en/personal-pitfall-knowledge/README.md) |
| Low token / Hardware | hardware-connection-check | Confirm debugger and peripheral connections before targeted checks | [中文](low_token/hardware/zh/hardware-connection-check/README.md) | [English](low_token/hardware/en/hardware-connection-check/README.md) |
| Learning | adaptive-learning-guide | Adapt teaching to purpose, background, prerequisites, and feedback | [中文](learning/zh/adaptive-learning-guide/README.md) | [English](learning/en/adaptive-learning-guide/README.md) |

```text
low_token/
  general/
    zh/<skill-name>/SKILL.md
    en/<skill-name>/SKILL.md
  hardware/
    zh/hardware-connection-check/SKILL.md
    en/hardware-connection-check/SKILL.md
learning/
  zh/adaptive-learning-guide/SKILL.md
  en/adaptive-learning-guide/SKILL.md
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

`personal-pitfall-knowledge` includes scripts, references, and tests; `adaptive-learning-guide` adds only references for on-demand teaching examples and maintenance scenarios. Other skills have no empty placeholder directories. Routine invocation reads `SKILL.md` and task-relevant resources; installation and maintenance use the README and AI guide.

## Installation and use

Install manually or give a prompt below to an AI assistant with local file and download tools. A web-only chat cannot install directly on your computer. Confirm discovery and invocation per host; interface YAML is optional and does not establish that all skills have been tested across hosts.

### Determine the installation directory

Current [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) recommends `~/.agents/skills/` for user skills and `.agents/skills/` for project skills. Existing environments may still load from `~/.codex/skills/` or `$CODEX_HOME/skills/`; follow the actual host configuration or skill list. Do not install duplicate names across discovery directories. Here, `<skills-dir>` means the confirmed user skill directory.

Read each selected skill's `AI_readme.md`, `README.md`, and `SKILL.md` first. Install one language per skill. Back up a same-name installation outside discovery directories before replacing the whole folder; preserve unrelated skills. Check installed files and host discovery. Restart the host if needed; a successful copy alone does not demonstrate invocation.

### Method one: Install all skills

1. [Download and extract the repository ZIP](https://github.com/Jungle-Bert/practical-agent-skills/archive/refs/heads/main.zip), or run `git clone https://github.com/Jungle-Bert/practical-agent-skills.git`.
2. Choose `en` or `zh`. Copy the four folders under `low_token/general/<language>/`, one under `low_token/hardware/<language>/`, and one under `learning/<language>/` separately into `<skills-dir>/`.
3. Each target is `<skills-dir>/<skill-name>/SKILL.md`: six skills total. Do not copy category/language parents or install all twelve bilingual editions. For usage reduction or learning alone, copy only skills from the corresponding directories.
4. `personal-pitfall-knowledge` needs Python 3.9+. For automatic troubleshooting lookup and capture, follow its README to integrate global rules. Store personal data outside the skill folder.

**Simple example:**

```text
Install all English skills in <repository folder>. Read README.en.md and AI_readme.md first.
```

Or attach the complete skill ZIP and say: “Install the English skills in this attachment, following its README and AI_readme.md.” A repository URL can replace the path; specify Chinese for Chinese editions. The English concise skill still defaults to Chinese replies unless another language is requested.

### Method two: Install one skill

1. Download/clone the repository and use only the desired folder, such as `low_token/general/en/project-readme-first/`. A local assistant may instead retrieve that complete folder alone.
2. Read its `AI_readme.md` and `README.md`; copy the entire folder as `<skills-dir>/project-readme-first/`, retaining `agents/`, `LICENSE`, and its actual resources.
3. Invoke `$project-readme-first` on hosts supporting `$skill-name`, or use the host's skill selector. No other skill is required; follow the selected skill's README for extra integration such as global rules.

**Simple example:**

```text
Install the skill in <individual skill folder>. Read README.md and AI_readme.md first.
```

You can also provide one complete skill folder or ZIP and say “Install this skill.” The AI follows its entry documents for installation and usage integration.

### Update an existing clone

Run `git remote set-url origin https://github.com/Jungle-Bert/practical-agent-skills.git` in an existing clone, then pull updates normally. Its local folder can keep its old name. Usage-reduction source paths now live under `low_token/`; installed skill names and user-level installation locations do not need to change with repository grouping.

## Contributions and repository permissions

A public repository can be viewed, downloaded, and forked by anyone. Direct pushes require the owner or a collaborator with write access and remain subject to branch rules; public visibility does not grant write access. See [GitHub permissions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository).

Others can fork and open a pull request for maintainer review. Keep both language editions, documentation, and interface metadata synchronized, complete validation, and exclude personal data and credentials.

## Source and maintenance

This project is the permanent maintenance home for personal skills. Codex writes, updates, applies, and validates skills, then uploads the user-selected scope to this repository's GitHub remote. Repository sources and locally installed copies are maintained separately. Publish only selected skills and their necessary supporting files. See [AGENTS.md](AGENTS.md) for project agreements.

The three general skills come from the author's existing local skills. `hardware-connection-check` was extracted from the local-device collaboration guidance in `user-assisted-operations`, with the author's requested ordering: ask about connections before searching for devices. The general edition no longer handles device connection checks.

The pitfall search tool requires Python 3.9+ standard library. Optional PITFALL_KB_ROOT selects the local database; the default is a fixed location under the user's Documents directory. Normal queries return only short results rather than all knowledge. See its [README](low_token/general/en/personal-pitfall-knowledge/README.md) for budgets, triggers, and usage. Personal entries are not published with the skill.

No build or deployment is needed. Keep both language editions, the index, and interface metadata in sync. See [AI_readme.md](AI_readme.md) for maintenance and validation guidance.

## License

Released under the [MIT License](LICENSE), allowing use, modification, and redistribution.
