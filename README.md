# Low Codex Skills

[English](README.en.md) | 中文

用于减少重复沟通、无效检索和上下文读取的个人 Codex 技能。技能分为 **通用** 与 **硬件** 两类，每个技能均提供中文与英文版本；不承诺固定比例的 token 节省。

## 技能目录

| 类别 | 技能 | 用途 | 中文 | English |
| --- | --- | --- | --- | --- |
| 通用 | concise-collaboration | 简洁回复，减少背景和过程重复 | [中文](general/zh/concise-collaboration/SKILL.md) | [English](general/en/concise-collaboration/SKILL.md) |
| 通用 | project-readme-first | 先读项目 Markdown，再定向查阅源码 | [中文](general/zh/project-readme-first/SKILL.md) | [English](general/en/project-readme-first/SKILL.md) |
| 通用 | user-assisted-operations | 协调高成本下载、文件准备和账号授权 | [中文](general/zh/user-assisted-operations/SKILL.md) | [English](general/en/user-assisted-operations/SKILL.md) |
| 硬件 | hardware-connection-check | 先确认仿真器、调试器与外设连接，再定向检查 | [中文](hardware/zh/hardware-connection-check/SKILL.md) | [English](hardware/en/hardware-connection-check/SKILL.md) |

```text
general/
  zh/<skill-name>/SKILL.md
  en/<skill-name>/SKILL.md
hardware/
  zh/hardware-connection-check/SKILL.md
  en/hardware-connection-check/SKILL.md
```

每个技能目录还包含 `agents/openai.yaml`，提供对应语言的界面说明。

## 安装与使用

将所选语言的**整个技能文件夹**复制到 `$CODEX_HOME/skills/`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills/`。例如将 `general/zh/project-readme-first/` 复制为 `~/.codex/skills/project-readme-first/`。

中英文版使用相同技能名称，每个技能只安装一种语言，避免同名冲突。复制前检查已有同名技能并备份；切换版本时替换整个对应文件夹。使用 `$project-readme-first`、`$concise-collaboration` 等名称显式调用，也可由 Codex 根据任务自动选择。

英文版翻译技能说明并保留行为约束；`concise-collaboration` 的默认回复语言仍为中文，用户明确要求其他语言时遵从用户要求。

## 来源与维护

三个通用技能来自作者已有的本地技能。`hardware-connection-check` 从 `user-assisted-operations` 的本地设备协作规则拆分，并按作者要求补充“先询问连接状态，再查找设备”的顺序；通用版不再承担设备连接检查。

这是技能文档仓库，不需要构建、部署或环境变量。修改时同步维护中英文版本、目录索引与界面说明；验证入口和维护约束见 [AI_readme.md](AI_readme.md)。

## 许可证

采用 [MIT License](LICENSE)，允许使用、修改和再分发。
