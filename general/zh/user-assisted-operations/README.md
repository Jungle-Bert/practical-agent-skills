# 用户协助操作

识别用户手动完成更省时的资源准备、下载或授权步骤，先推进独立工作，再提出明确操作请求。

## 独立安装

1. 获取本目录的完整文件夹，安装前先读 [AI_readme.md](AI_readme.md)、本文件和 [SKILL.md](SKILL.md)。不需要安装仓库中的其他技能。
2. 将整个文件夹复制为宿主用户级技能目录下的 `user-assisted-operations/`。当前 Codex 官方目录为 `~/.agents/skills/`；仍使用 `~/.codex/skills/` 或 `$CODEX_HOME/skills/` 的环境按宿主实际配置选择，避免在多个目录重复安装。
3. 只安装一种语言；替换前将已有同名目录备份到技能发现目录以外，替换整个目录，保留其他技能。
4. 检查目标 `SKILL.md` 可读并在宿主中发现该技能；未出现时重启宿主，再显式调用。

把文件夹路径或完整技能压缩包交给有本地文件工具的 AI，例如：

```text
帮我安装 <本技能文件夹路径> 中的 skill，先阅读 README.md 和 AI_readme.md。
```

普通网页聊天不能直接写入电脑，需要有本地文件工具的助手。宿主目录与发现方式见 [OpenAI 官方说明](https://learn.chatgpt.com/docs/build-skills)。

## 使用与边界

```text
请使用 $user-assisted-operations，先完成可独立推进的工作，再告诉我哪些资源准备由我手动完成更省事。
```

不把低成本常规操作转交给用户；已有明确执行授权时直接推进；硬件连接确认由专门技能处理。完整执行规则见 [SKILL.md](SKILL.md)。

## 文件与维护

- [README.md](README.md)：面向人的安装、用法和维护说明。
- [AI_readme.md](AI_readme.md)：AI 安装与维护导航，日常调用无需额外加载。
- [SKILL.md](SKILL.md)：触发描述与执行规则。
- [agents/openai.yaml](agents/openai.yaml)：宿主界面文字。
- [LICENSE](LICENSE)：MIT 许可证，单独复制或分发时保留。

无脚本或外部依赖，无需构建。修改时同步另一语言版本；可用 skill-creator 的 `quick_validate.py <skill-folder>` 校验入口，检查相对链接与界面 YAML。文档和静态校验不能证明宿主中的实际行为，需结合使用反馈验证。
