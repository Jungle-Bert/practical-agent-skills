# AI 项目导航 / AI Project Guide

- 范围 / Scope：省 token 的 Codex 技能文档仓库；3 个通用技能、1 个硬件技能，各有中文和英文版。事实来源是各目录的 `SKILL.md`。
- 阅读顺序 / Read order：先读本文件，再按语言读 `README.md` 或 `README.en.md`，最后只读与任务有关的 `SKILL.md` 及其 `agents/openai.yaml`。
- 目录 / Layout：`general/{zh,en}/` 放通用技能；`hardware/{zh,en}/` 放硬件技能；`LICENSE` 为 MIT 许可证。
- 入口 / Entry：每个技能由 `SKILL.md` 的 YAML `name`、`description` 与 Markdown 指令组成；`agents/openai.yaml` 提供界面文字。每个技能只安装一个语言版本。
- 依赖 / Dependencies：使用时无脚本依赖。验证可使用 Python、PyYAML 和 Codex skill-creator 自带的 `scripts/quick_validate.py`。
- 验证命令 / Validation：对每个技能目录执行 `python <skill-creator-path>/scripts/quick_validate.py <skill-folder>`；检查界面 YAML、相对链接和中英文行为一致性；执行 `git diff --check`。
- 构建与部署 / Build and deploy：无需构建或部署；发布通过普通 Git 提交与推送完成。不要上传本地凭据、个人绝对路径或无关技能。
- 修改约束 / Constraints：同步更新中英文内容与 README 索引。硬件连接请求先于设备搜索；用户已提供连接信息时不要重复询问；通用技能不重复承担硬件连接检查。
- 已知限制 / Limits：简洁沟通技能保留中文默认回复；英文技能是指令翻译。通用技能可能要求维护项目入口文档，是否节省 token 取决于任务。
- Last verified：2026-10-01；8 个技能入口和界面 YAML、目录配对、README 链接及 Git 空白检查。无运行时代码测试。
