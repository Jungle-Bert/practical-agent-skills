# AI 导航 / AI Navigation

- 范围：短索引查询与按需卡片读取；个人数据在独立库根目录，不在公开 skill。
- 安装阅读顺序：本导航 → [README.md](README.md) → [SKILL.md](SKILL.md)；单独复制本技能完整目录，按宿主发现路径安装，一种语言，同名备份放发现目录以外。依赖与全局触发接入见 README。
- 基础结构：README.md、AI_readme.md、SKILL.md、[agents/openai.yaml](agents/openai.yaml)、[LICENSE](LICENSE)；额外 scripts/references/tests 均为本技能所需资源。独立安装不要求其他技能。
- 正常调用只读 [SKILL.md](SKILL.md)，直接运行脚本；不加载本导航、README、脚本源码或整个 index.jsonl。维护开发时先读本导航和 [README.md](README.md)。
- 实际入库才读 [references/maintenance.md](references/maintenance.md) 与条目模板。
- `scripts/pitfalls.py`：search 只读短索引；get 只读所选卡片且检查哈希；index 更新单条元数据并保留其他记录。
- 依赖：Python 3.9+ 标准库，无网络服务。Python/PyYAML 仅用于 skill frontmatter 校验。
- 验证：`python -m unittest discover -s <skill>/tests`、skill-creator quick_validate、仓库 `git diff --check`；中英文脚本必须逐字一致。
- 不变量：search 不读卡片；正常知识输出 ≤3000 字符；无匹配不扫描详情；状态/边界必须保留；公开仓库不含个人数据库或个人绝对路径。
- 修改数据结构时同步中文/英文文档及模板。无构建/部署，发布为 Git 提交推送。
- Last verified：2026-10-02；统一入口结构、相对链接与脚本测试，真实发现及触发仍依赖宿主。
