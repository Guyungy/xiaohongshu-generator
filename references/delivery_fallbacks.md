# 交付回退方案（Delivery Fallbacks）

适用于：小红书内容生成完成后的打包与发送阶段。

## Telegram 文件发送回退

### 已验证问题
`message(action=send)` 在 Telegram 发送文件时，可能误报：

```text
Poll fields require action "poll"; use action "poll" instead of "send".
```

这不一定是 Telegram API 挂了，更可能是当前工具层/参数校验误判。

---

## 正确处理顺序

### 路径 1：最小参数工具发送
先尝试最小参数：
- action
- channel
- target
- media
- caption（可选）

如果成功，则结束。

### 路径 2：改用 `tar.gz`
如果 `zip` 不稳定，优先改打包成：

```text
<topic>.tar.gz
```

### 路径 3：切 OpenClaw CLI 发送
如果仍报 poll 误判，不要继续堆参数，直接改用：

```bash
openclaw message send \
  --channel telegram \
  --target '<chat-or-chat:topic>' \
  --media '/absolute/path/to/file'
```

该路径已在本项目中实测成功。

---

## 交付完成判定

满足以下条件才算交付成功：

- 文件已生成
- 打包已生成
- 实际发送成功
- 有返回的 messageId / chatId

如果只是本地生成完成，但未成功发送，不算完成。
