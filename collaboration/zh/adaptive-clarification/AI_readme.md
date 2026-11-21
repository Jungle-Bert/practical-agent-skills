# AI 导航：adaptive-clarification

- 范围：跨任务的自主澄清与反馈维护，支持用户主动要求追问；信息充分时直接推进。
- 安装／维护读本导航 → [README.md](README.md) → [SKILL.md](SKILL.md)。日常只加载 SKILL.md，读写反馈时才读 [references/feedback-records.md](references/feedback-records.md)。
- 安装：复制一种语言的完整技能目录到宿主实际发现位置，同名备份放发现目录外；检查入口、脚本、发现结果并说明调用方式，无需全局规则。用户要求替换时才备份停用旧 grill-me。
- 结构：统一 README、AI_readme、SKILL、[agents/openai.yaml](agents/openai.yaml)、[LICENSE](LICENSE)，另有 scripts/、references/ 和 tests/。界面 YAML 可选；默认 Markdown 只需文件工具，可选 JSON 脚本需 Python 3.9+ 标准库，无网络依赖。
- 澄清／新记录前先单独让用户选择：默认私有目录、指定目录、项目目录，也可仅对话；显示实际路径，未答复先等待，同任务明确选过不重复问。普通充分上下文问答不强制选址。
- [scripts/feedback.py](scripts/feedback.py)：按稳定 context 读当前 JSON 反馈、修订及删除；私有目录候选为 ~/.agent-feedback，可由 AGENT_FEEDBACK_ROOT 或 --root 指定所选根。用户选择仓库内位置后需 --allow-repository 并先排除 Git 跟踪；具体技能目录始终拒绝。
- 格式：新任务默认由 AI 直接维护 Markdown，无 Python 仍可落盘；已有 JSON 沿用，切换需用户要求／同意。每任务只有一份有效记录，路径、格式和 context 随交接保留；Markdown 模板及修订／删除规则见反馈说明。
- 不变量：先复用资料再问；不确定、委托、初稿、拒答、待补与验证分开；沉默不是同意，反馈不是执行授权；只写真实必要信息，不发布个人记录。
- 修改：双语脚本与 tests/test_feedback.py 逐字相同；语义、文档和界面同步。不要把用户资料或备份放入此目录。
- [references/behavior-checks.md](references/behavior-checks.md)：维护时走查主动询问、资料充分、状态更正与主题深度，不作为日常默认上下文。
- 验证：quick_validate；python -X utf8 -m unittest discover -s <skill>/tests；检查 YAML、相对链接、双语文件结构与 git diff --check。区分脚本实测、维护者走查与真实用户对话效果。
- Last verified：2026-11-21；脚本与 CLI 测试、入口、YAML、链接及维护者情境走查；持续对话和其他宿主发现待实际使用验证。
