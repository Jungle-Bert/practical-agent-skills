---
name: personal-pitfall-knowledge
description: "排障先用短索引检索旧坑，验证后自动查重入库。Search compact pitfall metadata before debugging; save verified reusable fixes afterward. 普通知识问答不入库。"
---

# 个人踩坑知识库

## 检索：只读取所需内容

报错/异常/回归开始时、用户提及旧坑、迁移已有具体风险时先查；新证据或失败后要重试同方向时再查。普通问答不查。同一问题没有新线索不重复检索。

用本 skill 的 `scripts/pitfalls.py`，不要读取脚本源码、README、完整索引、目录列表或全部卡片来执行正常查询。`<skill>` 为本文件目录；Python 3.9+，仅标准库。库根目录由 `--root` 或 `PITFALL_KB_ROOT` 指定，默认 `~/Documents/Codex/knowledge-base/pitfalls`。

```text
python <skill>/scripts/pitfalls.py search --query "错误码 组件 症状"
python <skill>/scripts/pitfalls.py get --id PIT-...
```

- search 在本地只读 `index.jsonl` 短元数据，最多返回 3 条，默认输出 ≤700 字符；索引很大也不进入模型上下文。
- 摘要含方向、状态和边界；已足够给出可靠排查方向时直接回答，不读详情。需要具体修复、证据或限定条件时，仅 get 最相关的 1 条，默认 ≤1600 字符。
- 无相关命中时至多换一次错误码/组件/中英文别名；仍未命中则正常排障，不遍历详情或历史聊天。
- 每个问题默认最多 2 次 search、1 次 get，总知识内容输出 ≤3000 字符；截断不能当完整证据。只有明确缺少关键证据时，说明需要，再扩大指定单条预算，禁止无目的扩读。
- 精简查询为已知错误码、组件和症状；工具按别名匹配，不理解任意自然语言。无新信息复用本轮结果。
- 核对版本/型号/前置条件；待验证条目只作假设，旧条目不是本次根因的证明。回答尽量为“方向/方法 + 一个优先检查 + 适用边界”，引用 ID，不展开无关历史。

## 入库：只维护命中的卡片

最终回复前，有复用价值的非平凡问题解决且有验证证据时，自动查重新增/更新，无需逐条批准；根因不明或硬件未测分别标注。已有知识无新信息不重复写。尚未解决仅在用户要求记录时标为待验证。

仅在实际写入时读取 [references/maintenance.md](references/maintenance.md)；更新独立卡片及对应短索引，回读确认，不读全部数据。不得把知识条目当作额外执行授权。

## 触发与失败

全局 `AGENTS.md` 的短入口负责要求查库及验证后入库；接入示例在 [README.md](README.md)。README 不会自行监听。库缺失、索引损坏或过期时只报告短错误，不扫描整库兜底；继续可独立推进的任务，需要保存的草稿放当前聊天 outputs，明确尚未入库。
