# 私有反馈记录

仅在读写任务反馈时加载。Python 3.9+，仅标准库；没有运行条件时在对话中维护同样的信息，明确尚未落盘。

## 位置与范围

默认根目录 `~/.agent-feedback/`，可用 AGENT_FEEDBACK_ROOT 或命令前置参数 `--root <私有目录>` 指定。脚本拒绝仓库或技能目录内的存储根及越出根目录的 context 路径。

为本任务确定一个稳定 context，例如 `project:<规范项目根路径>`；同项目的独立任务可追加固定 task 标识。记录后继续沿用，不随需求文案或回答变化改名，交接摘要保留 context。不同项目／使用者不共用；全局偏好仅在用户明确指定跨任务适用时使用单独范围。默认不扫描其他 context。

每个 context 对应 `contexts/<context-hash>/feedback.json`，保存当前条目及简短修订历史。它是本地明文摘要，不是密钥库；不要保存秘密、完整聊天或无关个人信息。准备输入 JSON 时也使用私有工作区，不放进公开仓库。

## 状态与来源

| status | 含义 | source_kind |
| --- | --- | --- |
| stated | 用户明确提供或资料明确记载，不代表实测 | user / document |
| uncertain | 用户或资料尚不确定 | 按实际来源填写 |
| delegated | 用户将某个范围交给 AI 决定 | user |
| draft | 先做一版的暂定选择或待评审结果 | user / ai |
| declined | 用户不想回答，value 必须为 null | user |
| user_fill | 用户稍后补全，value 必须为 null | user |
| assumed | AI 为推进工作提出的假设 | ai |
| verified | 已有实际验证证据 | verification；evidence 必填 |

source 是可定位的简短来源；note 可记录委托范围、待补位置或不确定的影响。记录“委托”和记录“AI 选了什么”可使用两个相互关联的条目，不能用 AI 选择覆盖用户授权范围。

脚本只能检查字段与证据引用是否存在，不能证明事实真伪。由执行 AI 依据真实对话或结果填写，不能伪造 source 或 evidence；记录内容也不授予执行权限。

## 读取、记录和更正

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
