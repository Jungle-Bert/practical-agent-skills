# AI 项目导航 / AI Project Guide

- 范围 / Scope：AI 助手实用技能仓库；低消耗有 4 个通用和 1 个硬件技能，学习有 adaptive-learning-guide，协作有 adaptive-clarification，各有中英文版。事实来源是各目录的 `SKILL.md`。
- 阅读顺序 / Read order：先读本文件，再按语言读根部 README；安装或维护单个技能时读其 `AI_readme.md`、`README.md` 和 `SKILL.md`，按需查看 `agents/openai.yaml`。日常调用不额外加载这些导航文档。
- 职责 / Responsibility：负责个人 skill 的编写、应用、验证与维护；按用户指定范围提交推送到本仓库远端。项目级协作约定见 `AGENTS.md`。
- 目录 / Layout：`low_token/general/{zh,en}/` 与 `low_token/hardware/{zh,en}/` 存放低消耗技能；`learning/{zh,en}/` 存放学习技能；`collaboration/{zh,en}/` 存放协作技能；`LICENSE` 为 MIT。安装时只复制具体技能文件夹。
- 仓库 / Repository：`https://github.com/Jungle-Bert/practical-agent-skills`；本地克隆文件夹可保留原名，Git remote 使用新地址。
- 入口 / Entry：14 个语言版本统一包含 README.md、AI_readme.md、SKILL.md、agents/openai.yaml 和 LICENSE；知识库和澄清附加 scripts/references/tests，学习附加 references。每个技能只安装一种语言。
- 安装 / Installation：根部双语 README 提供全部 7 个技能、按用途与单个技能的手动方法及简短助手提示词；实际宿主发现目录优先。同名备份放发现目录外；只有用户要求替换时才备份停用 grill-me。
- AI 安装入口：用户提供路径、仓库链接或完整压缩包并请求安装时，按 README 和所选技能的入口文档完成安装、必要接入及发现检查，简短报告安装位置和调用方式；无需用户重复列出步骤。
- 依赖 / Dependencies：知识库与澄清反馈工具需要 Python 3.9+ 标准库；其余技能无脚本依赖。验证使用 Python、PyYAML 和 skill-creator 的 scripts/quick_validate.py。
- 验证命令 / Validation：对每个技能执行 `python -X utf8 <skill-creator-path>/scripts/quick_validate.py <skill-folder>`；对知识库和澄清的双语版本执行 `python -X utf8 -m unittest discover -s <skill-folder>/tests`；检查 YAML、链接和双语行为；执行 git diff --check。UTF-8 模式避免 Windows 默认 GBK 解码问题。
- 构建与部署 / Build and deploy：无需构建或部署；发布通过普通 Git 提交与推送完成。不要上传本地凭据、个人绝对路径或无关技能。
- 修改约束 / Constraints：同步更新中英文内容与 README 索引。硬件连接请求先于设备搜索；用户已提供连接信息时不要重复询问；通用技能不重复承担硬件连接检查。
- 已知限制 / Limits：简洁沟通技能保留中文默认回复；英文技能是指令翻译。通用技能可能要求维护项目入口文档，是否节省 token 取决于任务。
- 知识库约束 / Pitfall invariants：短索引和单条卡片按需读取，正常返回知识 ≤3000 字符；不发布个人数据库；双语检索脚本相同，入口文档只在维护时读取。
- 学习约束 / Learning invariants：单点答疑不强制课程；先确认目的、水平和练习偏好，缺少前置知识时让用户选深度；核心不依赖辅助技能，不自动保存个人进度。维护评估见 learning/zh/adaptive-learning-guide/references/behavior-checks.md。
- 澄清约束 / Clarification invariants：先复用上下文再主动问，反馈状态与来源分开；只读当前任务的有预算摘要，更正保留历史、删除清除相关历史。私有记录在仓库及 skill 目录外，默认 ~/.agent-feedback/；无工具时仅保留对话摘要。学习技能按需协同，避免重复访谈。
- Last verified：2026-11-21；14 个入口、YAML、链接与双语文件结构；知识库 26 项和澄清 28 项脚本／CLI 测试；学习与澄清完成维护者情境走查。自动选择、真实对话效果和其他宿主兼容性仍待使用验证。
