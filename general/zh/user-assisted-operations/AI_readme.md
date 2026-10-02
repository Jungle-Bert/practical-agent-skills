# AI 导航：user-assisted-operations

- 范围：本目录是可独立安装的单一技能，识别用户手动完成更省时的资源准备、下载或授权步骤，先推进独立工作，再提出明确操作请求。
- 安装／维护阅读顺序：[AI_readme.md](AI_readme.md) → [README.md](README.md) → [SKILL.md](SKILL.md)；只在界面变更时查看 [agents/openai.yaml](agents/openai.yaml)。
- 日常调用只加载 SKILL.md；本导航与 README 不作为每次调用的额外上下文。
- 结构：README.md、AI_readme.md、SKILL.md、agents/openai.yaml、[LICENSE](LICENSE)。无脚本依赖、外部服务或构建步骤。
- 安装：使用宿主实际识别的用户级目录；复制整个技能文件夹，一种语言，同名替换前备份到发现目录以外；不复制仓库 general/zh 等父级层次。
- 不变量：不把低成本常规操作转交给用户；已有明确执行授权时直接推进；硬件连接确认由专门技能处理。
- 修改：同步另一语言版本、用法和界面说明；无需读取仓库中无关技能。
- 验证：skill-creator quick_validate；相对链接、界面 YAML、双语行为与 git diff --check；实际应用另检查宿主发现及使用结果。
- AI 收到安装请求时按 README 完成安装和必要接入，检查宿主发现结果，简短给出安装位置及调用示例。
- Last verified：2026-10-02；入口文档和结构检查。实际发现依赖宿主。
