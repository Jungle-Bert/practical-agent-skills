# 自适应需求澄清

AI 先复用资料和已知反馈，再判断是否主动询问；按工程、学习或创作等主题调整深度，并记录可更正的答复、委托、拒答和待补项。支持用户主动要求追问，也支持信息充分时直接执行。

## 安装与使用

将完整技能文件夹或压缩包交给有本地文件工具的 AI，例如：

```text
帮我安装 <本技能文件夹路径> 中的 skill，先阅读 README.md 和 AI_readme.md。
```

安装 AI 先读本文件、[AI_readme.md](AI_readme.md) 和 [SKILL.md](SKILL.md)。确认宿主发现目录后，只复制一种语言的完整 `adaptive-clarification/`，同名旧版先备份到发现目录以外，保留其他技能。检查宿主发现结果、入口和脚本，报告安装位置与调用方式。不要求修改全局规则；自动选用仍取决于宿主支持，不能保证每轮必然加载。

正文不依赖特定 AI 产品。`agents/openai.yaml` 是可选界面配置。新任务默认由 AI 直接维护 Markdown，只需文件读写工具，无需 Python；JSON 可选工具需要 Python 3.9+ 标准库，无网络或第三方依赖。没有文件工具时仍可澄清，用对话摘要并说明未落盘。

通常可以直接说明任务或提供相关情况；支持 `$skill-name` 的宿主也可显式调用：

```text
使用 $adaptive-clarification，先看项目资料，缺少关键信息再问我。
```

## 反馈怎样记录

- 开展澄清或保存新反馈前，若尚未选过位置，先单独询问：默认用户私有目录 `~/.agent-feedback/`、用户指定目录，或项目内目录（例如 `<项目>/.agent-feedback/`）；也可只保留在对话中。显示实际路径并等待选择，再问业务问题／写记录。同任务已明确选择时沿用，不重复问。
- 新任务默认 Markdown：由 AI 直接维护当前反馈与简短修订历史，无需 Python。JSON 是可选增强；已有任务继续沿用有效文件／格式，每任务只维护一份，切换需用户要求或同意。路径、格式和 context 随任务交接。
- 两种格式都遵从选址与 Git 排除规则，具体 skill 目录内禁止存个人数据。JSON 用 AGENT_FEEDBACK_ROOT 或 `--root` 指定所选根，仓库内另加 `--allow-repository`；Markdown 直接用文件工具维护，不运行 Python。
- 状态区分明确陈述、不确定、委托、暂定初稿、拒答、用户待补、AI 假设和实际验证；来源与证据另记。用户陈述不等于实测，工具不能代替事实核验。
- 默认只读有预算的当前摘要；更正保留旧状态和原因，删除请求清除该条及相关历史。记录内容不是执行授权。
- 不保存密钥、整段聊天或无关个人信息，不把记录上传 GitHub。用户不希望保存时只在对话中维护或停止记录。

命令与字段见 [反馈记录说明](references/feedback-records.md)。安装本技能本身不会创建虚构反馈；实际使用时按真实答复记录。

## 与其他技能及旧版的关系

本技能不强制依赖其他 skill。项目阅读可借助 project-readme-first，资源准备可借助 user-assisted-operations，学习时与 adaptive-learning-guide 共享相关反馈，避免重复访谈。

它可替代只接受显式调用的 grill-me。**只有用户要求替换时**，才在新版验证并安装后，把旧 grill-me 移到发现目录外保留备份；不要因普通安装而移走其他技能。备份和个人记录均不进入公共包。

## 文件与维护

- [SKILL.md](SKILL.md)：自动判断询问时机、深度和反馈处理。
- [AI_readme.md](AI_readme.md)：AI 安装与维护导航。
- [agents/openai.yaml](agents/openai.yaml)：可选界面说明。
- [scripts/feedback.py](scripts/feedback.py)：可选 JSON 记录、修订、限量读取和删除。
- [references/feedback-records.md](references/feedback-records.md)：按需读写说明。
- [references/behavior-checks.md](references/behavior-checks.md)：维护情境评估。
- `tests/test_feedback.py`：脚本单元与 CLI 测试；[LICENSE](LICENSE)：MIT 许可证。

无需构建。运行 `python -X utf8 -m unittest discover -s <skill>/tests`，使用 skill-creator 的 quick_validate，并检查 YAML、相对链接与情境行为。中英文脚本和测试逐字一致，说明语义同步。脚本测试不证明真实对话体验或所有宿主的兼容性。
