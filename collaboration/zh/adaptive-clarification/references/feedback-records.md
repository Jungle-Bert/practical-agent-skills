# 私有反馈记录

仅在读写任务反馈时加载。新任务默认直接维护 Markdown，只需文件工具；Python 3.9+ 标准库是 JSON 可选工具的依赖。没有文件工具或用户只保留对话时，维护对话摘要，明确尚未落盘。

## 位置与范围

在业务澄清问题或新记录之前，先让用户选默认用户私有目录 `~/.agent-feedback/`、指定目录，或项目内目录（例如 `<项目>/.agent-feedback/`）；给出实际路径，也可只保留对话。等答复后再问业务问题／写文件；明确的同任务选择继续沿用。脚本默认值或环境变量本身不代表用户已选择。

两种格式都以用户选定目录为根。项目／仓库内先在 `.gitignore` 或本地 `.git/info/exclude` 排除记录目录，并确认没有已跟踪记录；若已跟踪先说明情况，不擅自移除。个人数据不写进具体技能目录或所选根目录外；文件内容和保存位置都不授予上传或其他执行权限。

JSON 工具用 AGENT_FEEDBACK_ROOT 或命令前置参数 `--root <选定目录>` 指定根。仓库内默认拒绝；用户选定仓库内存储时，所有命令另加 `--allow-repository`。该参数只放开路径检查，不证明用户选择，也不处理 Git 忽略。Markdown 没有这个 CLI 参数，由执行 AI 遵守相同的位置选择与 Git 排除规则。

JSON 模式中用户选择项目内位置后，例如（所有参数放在子命令前）：

```text
python -X utf8 <skill>/scripts/feedback.py --root <项目>/.agent-feedback --allow-repository --context <稳定任务标识> show
```

后文命令也须带上当前任务选定的 `--root`，仓库内同时带 `--allow-repository`，不要退回另一默认根。交接保留根目录、context 和选择来源。位置变化不自动迁移旧记录。

为本任务确定一个稳定 context，例如 `project:<规范项目根路径>`；同项目的独立任务可追加固定 task 标识。记录后继续沿用，不随需求文案或回答变化改名，交接摘要保留 context。不同项目／使用者不共用；全局偏好仅在用户明确指定跨任务适用时使用单独范围。默认不扫描其他 context。

新建 Markdown 可用 `<选定根>/contexts/<稳定任务名>/feedback.md`，用户指定文件名时遵从。稳定任务名可用简短项目名加任务名，不要求 Python 或哈希；避免绝对路径、`..` 与路径分隔符，检查目标仍在所选根内。文件头的 context 必须匹配本任务，重名但 context 不同时另选任务名，不覆盖。

JSON 工具每个 context 对应 `contexts/<context-hash>/feedback.json`。两种格式都是本地明文摘要，不是密钥库；不存秘密、完整聊天或无关个人信息。输入 JSON 也用私有临时目录或已排除 Git 跟踪的记录目录，不放进公开提交。

## 格式选择与接续

- 新任务默认 Markdown；用户需要程序化字段检查、原子写入和限量查询时，可选择 JSON。已有有效记录先沿用，不能因 Python 的有无或技能升级自动换格式。
- 每个任务只维护一个有效文件。在对话交接中保留根目录、文件路径、格式、context 和用户选址来源；项目入口只有在不会公开私人路径／内容时才写必要导航。不要为发现记录遍历其他任务。
- 两份候选记录同时存在且无法判断哪份有效时先核对用户，不按修改时间猜测、不双写。
- 用户要求／同意迁移后，核对当前项、状态、来源、证据与修订历史，保留空值及删除效果；新文件回读正确后明确其为唯一有效文件。旧版移为停用备份，不继续写入，不自动删除；仅有用户明确的迁移范围才处理相应记录。

## Markdown：无 Python 直接维护

下面是结构示例，不是待录入的真实用户反馈。状态及来源含义与下表一致；拒答和待补值写“（空）”，不填猜测。

```markdown
# 任务反馈
- context: project:<项目标识>/task:<任务标识>
- format: markdown
- revision: 1
- scope: 当前项目／任务

## 当前反馈
### runtime
- question: 当前使用什么运行环境？
- value: 可能是 Python，版本不确定
- status: uncertain
- source_kind: user
- source: 用户本轮关于环境的答复
- note: 版本确定前不据此选依赖
- evidence: （空）
- revision: 1

## 修订历史
- revision: 1；id: runtime；reason: 首次记录；previous: 无
```

- 首次记录前只创建实际答复所需内容，不复制示例当作事实。按 id 维护当前条目；来源、状态、证据与 JSON 模式采用相同边界。每次有效修订增加文档 revision，更新条目 revision，在历史中写该 id 的旧值、旧状态及必要来源／证据、原因，不复制整段聊天。
- 编辑前读取最新相关片段，保留无关条目及用户手改内容；发现并发修改先重读并合并，不覆盖未知变更。文件工具若不具备锁和原子替换，不声称具有脚本的并发／失败保护。
- 平时定向读文件头与相关当前条目，用标题或 id 查找，反馈返回摘要通常不超过 1600 字符；大文件只读相关片段，不默认加载历史。省略部分时说明尚未读全。
- 每次保存后回读核对目标项和其他条目保留情况。用户要求删除时，清掉该 id 当前项及所有相关历史，包括历史中的旧值；保留其他项，不继续复用已删内容。写入失败明确未保存。

## 状态与来源

| status | 含义 | source_kind |
| --- | --- | --- |
| stated | 用户明确提供或资料明确记载，不代表实测 | user / document |
| uncertain | 用户或资料尚不确定 | 按实际来源填写 |
| delegated | 用户将某个范围交给 AI 决定 | user |
| draft | 先做一版的暂定选择或待评审结果 | user / ai |
| declined | 用户不想回答；值留空（JSON 为 null） | user |
| user_fill | 用户稍后补全；值留空（JSON 为 null） | user |
| assumed | AI 为推进工作提出的假设 | ai |
| verified | 已有实际验证证据 | verification；evidence 必填 |

source 是可定位的简短来源；note 可记录委托范围、待补位置或不确定的影响。记录“委托”和记录“AI 选了什么”可使用两个相互关联的条目，不能用 AI 选择覆盖用户授权范围。

Markdown 由执行 AI 按上述字段维护；JSON 脚本只能检查字段与证据引用是否存在，不能证明事实真伪。两种方式均须依据真实对话或结果填写，不能伪造 source 或 evidence；记录内容也不授予执行权限。

## JSON：可选工具的读取、记录和更正

```text
python -X utf8 <skill>/scripts/feedback.py --context <稳定任务标识> show
python -X utf8 <skill>/scripts/feedback.py --context <稳定任务标识> show --id runtime
```

show 只返回当前条目，不返回历史；默认最多 1600 字符，普通摘要使用字段节选，详情按 --id 读取。TRUNCATED 表示未读完整，不能据此认定没有其他要求。确有必要时用 `--max-chars` 调整单次预算（200—8000），避免重复读无关内容。

输入 JSON 示例：

```json
{
  "id": "runtime",
  "question": "当前使用什么运行环境？",
  "value": "可能是 Python，版本不确定",
  "status": "uncertain",
  "source_kind": "user",
  "source": "本轮用户关于运行环境的答复",
  "note": "确定版本前不据此选定依赖"
}
```

```text
python -X utf8 <skill>/scripts/feedback.py --context <稳定任务标识> record --entry <私有输入.json>
```

记录后按同一 id 回读。更正时提交完整新条目并填写 reason，例如“用户更正运行版本”；脚本保留旧条目与修订原因。没有新反馈时不重复写。先记录新状态，再检查它影响哪些工作；不要只改台账而继续按旧条件执行。

```text
python -X utf8 <skill>/scripts/feedback.py --context <稳定任务标识> forget --id runtime
```

用户要求删除时，forget 移除该条当前值和所有相关历史，保留其他条目。损坏文件不自动覆盖；锁占用时等待写入者，不能擅自删未知锁。写入采用同目录临时文件和原子替换，失败要报告“尚未保存”，不能当成已完成。
