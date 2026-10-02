# 简洁协作

在用户要求简短回答、减少 token 或简洁沟通时，减少背景重复并保持行动明确。

## 独立安装

1. 获取本目录的完整文件夹，安装前先读 [AI_readme.md](AI_readme.md)、本文件和 [SKILL.md](SKILL.md)。不需要安装仓库中的其他技能。
2. 将整个文件夹复制为宿主用户级技能目录下的 `concise-collaboration/`。当前 Codex 官方目录为 `~/.agents/skills/`；仍使用 `~/.codex/skills/` 或 `$CODEX_HOME/skills/` 的环境按宿主实际配置选择，避免在多个目录重复安装。
3. 只安装一种语言；替换前将已有同名目录备份到技能发现目录以外，替换整个目录，保留其他技能。
4. 检查目标 `SKILL.md` 可读并在宿主中发现该技能；未出现时重启宿主，再显式调用。

可把以下提示词交给有本地文件读写权限的 Codex／GPT 助手，替换下载目录：

```text
请安装我已下载到 <本技能文件夹> 的 concise-collaboration 技能。
先阅读 AI_readme.md、README.md 和 SKILL.md，确认文件完整、依赖和宿主实际识别的用户级技能目录。
只安装这个文件夹中的语言版本。将同名旧版本备份到发现目录以外，再复制完整文件夹；不要把两种语言同时安装。
检查安装后的文件和技能发现结果，报告安装路径与未完成项。不要改动无关技能或全局规则。
```

普通网页聊天不能直接写入电脑，需要有本地文件工具的助手。宿主目录与发现方式见 [OpenAI 官方说明](https://learn.chatgpt.com/docs/build-skills)。

## 使用与边界

```text
请使用 $concise-collaboration，简短汇报这个任务的结论、验证和剩余问题。
```

默认中文，用户指定其他语言时遵从；正在测试时的报告先作为观察记录，除非用户明确要求调查或修复。完整执行规则见 [SKILL.md](SKILL.md)。

## 文件与维护

- [README.md](README.md)：面向人的安装、用法和维护说明。
- [AI_readme.md](AI_readme.md)：AI 安装与维护导航，日常调用无需额外加载。
- [SKILL.md](SKILL.md)：触发描述与执行规则。
- [agents/openai.yaml](agents/openai.yaml)：宿主界面文字。
- [LICENSE](LICENSE)：MIT 许可证，单独复制或分发时保留。

无脚本或外部依赖，无需构建。修改时同步另一语言版本；可用 skill-creator 的 `quick_validate.py <skill-folder>` 校验入口，检查相对链接与界面 YAML。文档和静态校验不能证明宿主中的实际行为，需结合使用反馈验证。
