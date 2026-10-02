# Low Codex Skills

[English](README.en.md) | 中文

用于减少重复沟通、无效检索和上下文读取的个人 Codex 技能。技能分为 **通用** 与 **硬件** 两类，每个技能均提供中文与英文版本；不承诺固定比例的 token 节省。

## 技能目录

| 类别 | 技能 | 用途 | 中文 | English |
| --- | --- | --- | --- | --- |
| 通用 | concise-collaboration | 简洁回复，减少背景和过程重复 | [中文](general/zh/concise-collaboration/README.md) | [English](general/en/concise-collaboration/README.md) |
| 通用 | project-readme-first | 先读项目 Markdown，再定向查阅源码 | [中文](general/zh/project-readme-first/README.md) | [English](general/en/project-readme-first/README.md) |
| 通用 | user-assisted-operations | 协调高成本下载、文件准备和账号授权 | [中文](general/zh/user-assisted-operations/README.md) | [English](general/en/user-assisted-operations/README.md) |
| 通用 | personal-pitfall-knowledge | 短索引定位旧坑，按需读取卡片，验证后自动入库 | [中文](general/zh/personal-pitfall-knowledge/README.md) | [English](general/en/personal-pitfall-knowledge/README.md) |
| 硬件 | hardware-connection-check | 先确认仿真器、调试器与外设连接，再定向检查 | [中文](hardware/zh/hardware-connection-check/README.md) | [English](hardware/en/hardware-connection-check/README.md) |

```text
general/
  zh/<skill-name>/SKILL.md
  en/<skill-name>/SKILL.md
hardware/
  zh/hardware-connection-check/SKILL.md
  en/hardware-connection-check/SKILL.md
```

每个技能使用相同的基础结构，单独复制一个文件夹即可安装：

```text
<skill-name>/
  README.md                 人类安装、使用与维护说明
  AI_readme.md              AI 安装与维护导航
  SKILL.md                  触发描述与执行规则
  agents/openai.yaml        界面说明
  LICENSE                   MIT 许可证
  scripts/                  按需：可执行工具
  references/               按需：维护说明与模板
  tests/                    按需：工具测试
```

目前只有 `personal-pitfall-knowledge` 需要后三个目录，不给其他技能添加空目录。日常调用只读 `SKILL.md` 及当前任务所需资源；安装或维护时才读 README 和 AI 导航。

## 安装与使用

支持手动安装，也可把下方提示词交给有本地文件读写和下载权限的 Codex／GPT 助手。普通网页聊天无法直接安装到电脑。

### 先确定安装目录

当前 [OpenAI 官方文档](https://learn.chatgpt.com/docs/build-skills) 推荐用户级 `~/.agents/skills/`，项目级 `.agents/skills/`。已有环境可能仍从 `~/.codex/skills/` 或 `$CODEX_HOME/skills/` 加载，应以宿主实际配置或技能列表为准；不要同时向多个发现目录安装同名技能。本文用 `<skills-dir>` 表示已确认的用户级目录。

先读目标技能的 `AI_readme.md`、`README.md` 和 `SKILL.md`。每个技能只安装一种语言；同名旧版先备份到技能发现目录以外，再替换整个目录，保留无关技能。安装完成后检查文件完整性及宿主技能列表，未发现时重启宿主再检查；复制成功本身不代表已触发。

### 方法一：安装全部技能

1. [下载仓库 ZIP](https://github.com/Jungle-Bert/low_codex_skills/archive/refs/heads/main.zip) 并解压，或执行 `git clone https://github.com/Jungle-Bert/low_codex_skills.git`。
2. 选择 `zh` 或 `en`；将 `general/<语言>/` 下 4 个技能文件夹和 `hardware/<语言>/` 下 1 个技能文件夹分别复制到 `<skills-dir>/`。
3. 目标是 `<skills-dir>/<skill-name>/SKILL.md`，共 5 个技能；不要复制 `general`、`hardware` 或语言父目录，也不要把 10 个双语版本都装进去。
4. `personal-pitfall-knowledge` 需要 Python 3.9+；需要自动排障检索及入库时，按其 README 接入全局规则。个人数据库保存在技能文件夹之外。

**交给本地助手的提示词：**

```text
请从 https://github.com/Jungle-Bert/low_codex_skills 安装全部技能的中文版本。
可以克隆或下载 ZIP；如果已有完整本地副本则复用。先读仓库 AI_readme.md 和 README.md，
再读 general/zh/ 与 hardware/zh/ 下每个技能的 AI_readme.md、README.md 和 SKILL.md。
确认当前宿主实际识别的用户级技能目录，只安装 concise-collaboration、project-readme-first、
user-assisted-operations、personal-pitfall-knowledge、hardware-connection-check 这 5 个技能。
同名旧版先备份到发现目录以外，再复制完整文件夹，保留无关技能；不安装英文版。
检查 Python 3.9+；按踩坑知识库 README 将触发规则合并到宿主实际加载的全局 AGENTS.md，
保留已有规则和用户数据，不覆盖整个文件；没有知识库时说明初始化要求，不假称已能检索。
核对安装文件、宿主发现结果，报告各技能安装路径、备份位置和未完成项。
```

要装英文版，将提示词中的“中文／zh”替换为“英文／en”；英文简洁沟通技能仍默认中文回复，用户明确指定其他语言时遵从。已下载时把提示词第一句改成“请从我已解压到 <仓库目录> 的仓库安装全部中文技能”，无需再次下载。

### 方法二：只安装一个技能

1. 下载仓库 ZIP／克隆后，只使用目标技能目录，例如 `general/zh/project-readme-first/`。也可让本地助手仅获取该目录的完整内容。
2. 阅读该目录的 `AI_readme.md` 和 `README.md`，将整个目录复制为 `<skills-dir>/project-readme-first/`，保留 `agents/`、`LICENSE` 以及该技能实际包含的资源。
3. 使用 `$project-readme-first` 显式调用，或让 Codex 按任务选择。单独安装不要求其他 skill；全局规则等附加接入按所选 skill 的 README 处理。

**交给本地助手的提示词：**

```text
请只安装 https://github.com/Jungle-Bert/low_codex_skills/tree/main/general/zh/project-readme-first
中的 project-readme-first 中文技能。可克隆或下载，但只安装这个技能。
先读该目录 AI_readme.md、README.md 和 SKILL.md，确认完整资源和宿主实际识别的用户级技能目录。
同名旧版先备份到发现目录以外，再复制完整文件夹，保留 LICENSE；不安装其他技能或英文版。
不改动无关全局规则。检查安装文件和宿主发现结果，报告路径、备份和未完成项。
```

替换 URL、技能名和语言即可安装其他技能。只有下载好的单个技能文件夹时，直接使用其 README 内的离线安装提示词。

## 贡献与仓库权限

公开仓库允许所有人查看、下载和 Fork。直接向本仓库推送需所有者或获授权协作者的写入权限，并受分支规则约束；公开不等于任何人都能直接上传。[GitHub 权限说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository)

其他人可 Fork 后提交 Pull Request，由维护者审核合并。贡献时同步中英文文档、界面说明并完成验证，不提交个人数据库或凭据。

## 来源与维护

本项目作为个人 skill 的固定维护入口，由 Codex 负责 skill 的编写、更新、应用和验证，并按用户指定范围上传到本仓库的 GitHub 远端。仓库源码与本机安装目录分别维护；只发布指定 skill 及其必要关联文件。项目级约定见 [AGENTS.md](AGENTS.md)。

三个通用技能来自作者已有的本地技能。`hardware-connection-check` 从 `user-assisted-operations` 的本地设备协作规则拆分，并按作者要求补充“先询问连接状态，再查找设备”的顺序；通用版不再承担设备连接检查。

知识库技能的检索工具需要 Python 3.9+ 标准库；`PITFALL_KB_ROOT` 可选指定本地数据目录，默认使用用户 Documents 下固定位置。正常查询仅返回短结果，不读取全部知识进上下文；详细预算、触发入口和用法见其 [README](general/zh/personal-pitfall-knowledge/README.md)。个人知识记录不随 skill 发布。

仓库无需构建或部署。修改时同步维护中英文版本、目录索引与界面说明；验证入口和维护约束见 [AI_readme.md](AI_readme.md)。

## 许可证

采用 [MIT License](LICENSE)，允许使用、修改和再分发。
