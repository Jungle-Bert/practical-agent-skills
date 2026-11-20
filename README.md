# Practical Agent Skills

[English](README.en.md) | 中文

面向 AI 助手的实用技能集，包含 **降低不必要消耗** 和 **学习引导** 两类用途。低消耗技能目前位于 `general/` 和 `hardware/`，学习技能位于 `learning/`。每个技能提供中文与英文版；不承诺固定比例的 token 或额度节省，具体宿主兼容性以实际验证为准。

## 技能目录

| 类别 | 技能 | 用途 | 中文 | English |
| --- | --- | --- | --- | --- |
| 通用 | concise-collaboration | 简洁回复，减少背景和过程重复 | [中文](general/zh/concise-collaboration/README.md) | [English](general/en/concise-collaboration/README.md) |
| 通用 | project-readme-first | 先读项目 Markdown，再定向查阅源码 | [中文](general/zh/project-readme-first/README.md) | [English](general/en/project-readme-first/README.md) |
| 通用 | user-assisted-operations | 协调高成本下载、文件准备和账号授权 | [中文](general/zh/user-assisted-operations/README.md) | [English](general/en/user-assisted-operations/README.md) |
| 通用 | personal-pitfall-knowledge | 短索引定位旧坑，按需读取卡片，验证后自动入库 | [中文](general/zh/personal-pitfall-knowledge/README.md) | [English](general/en/personal-pitfall-knowledge/README.md) |
| 硬件 | hardware-connection-check | 先确认仿真器、调试器与外设连接，再定向检查 | [中文](hardware/zh/hardware-connection-check/README.md) | [English](hardware/en/hardware-connection-check/README.md) |
| 学习 | adaptive-learning-guide | 按目的与水平逐步带学，补前置并随反馈调整路线 | [中文](learning/zh/adaptive-learning-guide/README.md) | [English](learning/en/adaptive-learning-guide/README.md) |

```text
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

`personal-pitfall-knowledge` 包含 scripts、references 和 tests；`adaptive-learning-guide` 只额外包含按需教学示例与验证场景的 references。不给其他技能添加空目录。日常调用只读 `SKILL.md` 及当前任务所需资源；安装或维护时才读 README 和 AI 导航。

## 安装与使用

支持手动安装，也可把下方提示词交给有本地文件读写和下载权限的 AI 助手。普通网页聊天无法直接安装到电脑；不同宿主的技能发现与调用方式需分别确认，界面 YAML 可选，不能据此认定所有技能已跨宿主实测。

### 先确定安装目录

当前 [OpenAI 官方文档](https://learn.chatgpt.com/docs/build-skills) 推荐用户级 `~/.agents/skills/`，项目级 `.agents/skills/`。已有环境可能仍从 `~/.codex/skills/` 或 `$CODEX_HOME/skills/` 加载，应以宿主实际配置或技能列表为准；不要同时向多个发现目录安装同名技能。本文用 `<skills-dir>` 表示已确认的用户级目录。

先读目标技能的 `AI_readme.md`、`README.md` 和 `SKILL.md`。每个技能只安装一种语言；同名旧版先备份到技能发现目录以外，再替换整个目录，保留无关技能。安装完成后检查文件完整性及宿主技能列表，未发现时重启宿主再检查；复制成功本身不代表已触发。

### 方法一：安装全部技能

1. [下载仓库 ZIP](https://github.com/Jungle-Bert/low_codex_skills/archive/refs/heads/main.zip) 并解压，或执行 `git clone https://github.com/Jungle-Bert/low_codex_skills.git`。
2. 选择 `zh` 或 `en`；将 `general/<语言>/` 下 4 个、`hardware/<语言>/` 下 1 个和 `learning/<语言>/` 下 1 个技能文件夹分别复制到 `<skills-dir>/`。
3. 目标是 `<skills-dir>/<skill-name>/SKILL.md`，共 6 个技能；不要复制用途或语言父目录，也不要把 12 个双语版本都装进去。只需要低消耗或学习用途时，可仅复制对应目录中的技能。
4. `personal-pitfall-knowledge` 需要 Python 3.9+；需要自动排障检索及入库时，按其 README 接入全局规则。个人数据库保存在技能文件夹之外。

**简单示例：**

```text
帮我安装 <仓库文件夹路径> 中的全部中文 skills，先阅读 README.md 和 AI_readme.md。
```

也可以直接发送完整技能压缩包，并说：“帮我安装附件中的中文 skills，按里面的 README.md 和 AI_readme.md 操作。”路径可替换为仓库链接；需要英文版时说明安装英文版。英文简洁沟通技能仍默认中文回复，用户指定其他语言时遵从。

### 方法二：只安装一个技能

1. 下载仓库 ZIP／克隆后，只使用目标技能目录，例如 `general/zh/project-readme-first/`。也可让本地助手仅获取该目录的完整内容。
2. 阅读该目录的 `AI_readme.md` 和 `README.md`，将整个目录复制为 `<skills-dir>/project-readme-first/`，保留 `agents/`、`LICENSE` 以及该技能实际包含的资源。
3. 在支持 `$skill-name` 的宿主中使用 `$project-readme-first` 显式调用，其他宿主按其技能选择方式使用。单独安装不要求其他 skill；全局规则等附加接入按所选 skill 的 README 处理。

**简单示例：**

```text
帮我安装 <单个 skill 文件夹路径> 中的 skill，先阅读 README.md 和 AI_readme.md。
```

也可以发送单个技能的完整文件夹或压缩包，说“帮我安装这个 skill”。AI 按该技能的入口文档完成安装与使用接入。

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
