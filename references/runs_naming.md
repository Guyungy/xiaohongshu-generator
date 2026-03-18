# 运行目录规范（Runs Naming）

适用于：`output/runs/` 下的新产出目录命名。

## 目标
让每次新任务的产出：
- 可追踪
- 可归档
- 可区分 persona / topic / 日期
- 不再直接堆在 `output/` 根目录

---

## 推荐目录格式

### 标准格式

```text
output/runs/YYYYMMDD-<persona-slug>-<topic-slug>/
```

示例：

```text
output/runs/20260318-mrwong-watch-opencalw/
output/runs/20260318-zhangjie-school-selection/
```

---

## slug 规则

### persona-slug 建议
- `mrwong`
- `zhangjie`
- `edudaily`
- `sugarbaby`
- `artist`

### topic-slug 建议
- 只保留核心主题，不要过长
- 用英文或拼音短词连接
- 避免空格和复杂符号

---

## 每次 run 目录建议内容

```text
output/runs/YYYYMMDD-<persona-slug>-<topic-slug>/
├── 01.svg
├── 02.svg
├── ...
├── 01.png
├── 02.png
├── ...
├── post.md
├── brief.md              # 可选
├── marketing_final.md    # 可选
└── final.tar.gz          # 可选
```

---

## 使用规则

- 新任务默认写入 `output/runs/`
- 老任务不要回写到 `output/archive/legacy/`
- 若只是临时试稿，也建议进入单独 run 目录，不要散落在 skill 根目录
