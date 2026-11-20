# AI 导航：adaptive-learning-guide

- 范围：独立的对话式学习技能；根据目的、水平、前置知识和学习反馈调整路线，主体不绑定具体 AI 产品。
- 安装／维护先读本导航 → [README.md](README.md) → [SKILL.md](SKILL.md)。日常教学只加载 SKILL.md，按需读取教学示例。
- 安装：确认宿主支持与实际发现目录，复制一种语言的完整技能文件夹；同名备份放发现目录外，保留其他技能；检查发现结果，说明路径与调用方法。没有全局规则接入要求。
- 结构：README.md、AI_readme.md、SKILL.md、[agents/openai.yaml](agents/openai.yaml)、[LICENSE](LICENSE)、references/。没有脚本、必装依赖或构建步骤，界面 YAML 不属于跨宿主通用要求。
- [references/teaching-patterns.md](references/teaching-patterns.md)：用途差异、前置缺口和交接示例，遇到相关场景才读。
- [references/behavior-checks.md](references/behavior-checks.md)：维护时评估真实响应的场景；不把它作为日常教学指令，不用字符串匹配代替行为验证。
- 不变量：单点答疑不强制课程；前置缺口由用户选择深度；关闭练习仍能学习；保留原任务主线；不把已讲当掌握，不假称跨对话记忆。
- 数据与辅助：个人材料与进度不进入公开 skill；文件保存按用户请求。辅助技能可选且遵循各自触发条件，缺少时仍独立完成教学。
- 修改：同步另一语言版本和 README；只在界面变化时编辑 agents/openai.yaml。记录结构检查、情境走查与真实带学验证的不同证据范围。
- 验证：skill-creator quick_validate、界面 YAML、相对链接、git diff --check；按需走查验证场景。实际教学和跨宿主发现不能只靠静态检查证明。
- Last verified：2026-11-20；入口、界面 YAML、链接与维护情境走查；真实长期带学效果和其他宿主兼容性待使用验证。
