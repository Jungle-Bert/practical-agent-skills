# 个人踩坑知识库：低 token 检索

## 用途与结构

用短索引先给排查方向，再按需读取一条卡片。默认不读取全库、全索引或脚本源码；模型只收到有限查询结果。省的是进入上下文的内容，不承诺固定 token 比例；字符预算也不是精确 tokenizer 计数。

```text
<knowledge-root>/
  index.jsonl             短摘要与关键词；只供本地工具检索
  entries/PIT-....md       独立详细卡片
  archive/                旧库快照；查询不读取
```

Skill 目录含短 `SKILL.md`、`scripts/pitfalls.py`、写入专用 references、界面 YAML 和 AI 导航。只安装一种语言到 `$CODEX_HOME/skills/personal-pitfall-knowledge`，默认 `~/.codex/skills/`。

## 触发要求与接入

把以下短规则加入全局 `~/.codex/AGENTS.md`，实际 skill 路径按安装位置填写：

```text
报错/异常/回归、旧坑复发、迁移已有具体风险时，先读取已安装 personal-pitfall-knowledge/SKILL.md，通过短索引检索。
新证据或失败后准备重复同方向尝试时再查；普通问答和无新线索不反复查。
解决并验证了可复用问题后，按该 skill 查重、自动更新卡片与短索引、回读确认；无需逐条批准。
默认只返回最多3条短结果、按需读取1条详情，知识内容总输出不超过3000字符，禁止全库遍历进上下文。
```

README 描述规则，SKILL 执行规则，全局入口要求触发；没有后台监听任务。也可显式 `$personal-pitfall-knowledge`。触发依赖宿主加载全局入口和本地路径可用。

## 使用与预算

Python 3.9+，仅标准库；库根目录可用 `--root` 或环境变量 `PITFALL_KB_ROOT`，默认用户目录下 `Documents/Codex/knowledge-base/pitfalls`。

```text
python <skill>/scripts/pitfalls.py --root <knowledge-root> search --query "C1041 PDB"
python <skill>/scripts/pitfalls.py --root <knowledge-root> get --id PIT-...
```

search 每次输出 ≤700 字符、最多 3 条；get 默认 ≤1600 字符。正常流程一查零读或一查一读；至多换关键词再查一次，总 ≤3000 字符。`--max-chars` 仅用于有明确缺失证据时扩大单条预算。字符预算包括结果文字，不包括工具调用/skill 加载或对话本身；无新线索复用结果。

摘要已足够时回答准确方向与一个优先检查；有歧义时核对目标卡片的状态/环境，避免将待验证硬件方案说成实机已通过。`NO_MATCH` 后不自动扫描卡片；`STALE_INDEX` 说明目标正文与索引不同步，按写入规则修复目标记录。

## 写入与验证

只在实际入库时读取 [references/maintenance.md](references/maintenance.md)。先保存卡片，再用 `index --metadata <metadata.json>` 更新短索引和哈希，get 回读确认。更新工具使用锁与原子替换，不上传个人数据。

结构校验可运行 skill-creator 的 `quick_validate.py`。运行测试为 `python -m unittest discover -s <skill>/tests`，覆盖命中排序、不读详情、预算、失效索引和写入保留旧记录。知识库是用户自己的本地数据；本仓库不附带作者的知识记录、绝对个人路径或凭据。
