# AI 项目导航 / AI Project Guide

- 范围 / Scope：省 token 的 Codex 技能仓库；4 个通用技能、1 个硬件技能，各有中文和英文版。事实来源是各目录的 `SKILL.md`。
- 阅读顺序 / Read order：先读本文件，再按语言读根部 README；安装或维护单个技能时读其 `AI_readme.md`、`README.md` 和 `SKILL.md`，按需查看 `agents/openai.yaml`。日常调用不额外加载这些导航文档。
- 职责 / Responsibility：负责个人 skill 的编写、应用、验证与维护；按用户指定范围提交推送到本仓库远端。项目级协作约定见 `AGENTS.md`。
- 目录 / Layout：`general/{zh,en}/` 放通用技能；`hardware/{zh,en}/` 放硬件技能；`LICENSE` 为 MIT 许可证。
- 入口 / Entry：10 个语言版本统一包含 `README.md`、`AI_readme.md`、`SKILL.md`、`agents/openai.yaml` 和 `LICENSE`；仅知识库技能附加 scripts/references/tests。每个技能只安装一个语言版本。
- 安装 / Installation：根部双语 README 提供全部 5 个技能和单个技能的手动方法、在线／离线助手提示词；宿主实际发现目录优先，当前官方为 `~/.agents/skills`，已有环境可能使用 `.codex/skills`。同名备份放发现目录以外。
- 依赖 / Dependencies：知识库检索工具需要 Python 3.9+ 标准库；其他技能无脚本依赖。验证使用 Python、PyYAML 和 Codex skill-creator 自带的 `scripts/quick_validate.py`。
- 验证命令 / Validation：对每个技能目录执行 `python -X utf8 <skill-creator-path>/scripts/quick_validate.py <skill-folder>`；对知识库技能执行 `python -X utf8 -m unittest discover -s <skill-folder>/tests`；检查界面 YAML、相对链接和中英文行为一致性；执行 `git diff --check`。UTF-8 模式避免 Windows 默认 GBK 导致 UnicodeDecodeError。
- 构建与部署 / Build and deploy：无需构建或部署；发布通过普通 Git 提交与推送完成。不要上传本地凭据、个人绝对路径或无关技能。
- 修改约束 / Constraints：同步更新中英文内容与 README 索引。硬件连接请求先于设备搜索；用户已提供连接信息时不要重复询问；通用技能不重复承担硬件连接检查。
- 已知限制 / Limits：简洁沟通技能保留中文默认回复；英文技能是指令翻译。通用技能可能要求维护项目入口文档，是否节省 token 取决于任务。
- 知识库约束 / Pitfall invariants：短索引和单条卡片按需读取，正常返回知识 ≤3000 字符；不发布个人数据库；双语检索脚本相同，入口文档只在维护时读取。
- Last verified：2026-10-02；10 个技能入口、独立 README/AI 导航/LICENSE、界面 YAML、双语目录、相对链接、知识库脚本单元测试与 Git 空白检查。实际安装发现依赖目标宿主。
