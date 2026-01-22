# 浏览器自动化方案使用指南

完全自动化的小红书内容提取工具，一次登录，永久使用！

---

## 🎯 方案优势

- ✅ **一次登录，永久使用** - 登录状态自动保存
- ✅ **真实浏览器环境** - 完全模拟人工操作
- ✅ **自动提取内容** - 无需手动复制粘贴
- ✅ **支持所有小红书链接** - 包括短链接和完整链接

---

## 📦 安装（已完成）

```bash
# 1. 安装 Playwright
pip3 install playwright --user

# 2. 安装浏览器
python3 -m playwright install chromium
```

✅ 安装已完成！

---

## 🚀 使用方法

### 首次使用（需要登录）

```bash
python3 ~/.claude/skills/xiaohongshu-content-generator/tools/fetch_xhs_auto.py http://xhslink.com/o/2DIltcAJA2e
```

**流程：**
1. 浏览器自动打开小红书网站
2. 你在浏览器中手动登录
3. 登录完成后，返回终端按回车
4. 工具自动访问目标链接并提取内容
5. 登录状态自动保存

### 后续使用（自动登录）

```bash
python3 ~/.claude/skills/xiaohongshu-content-generator/tools/fetch_xhs_auto.py <任意小红书链接>
```

**流程：**
1. 自动使用保存的登录状态
2. 自动访问链接
3. 自动提取内容
4. 内容保存到文件

---

## 📝 提取的内容

工具会提取以下信息：
- 标题
- 作者
- 正文内容
- 标签

提取的内容会：
1. 显示在终端
2. 保存到文件：`~/.claude/skills/xiaohongshu-content-generator/data/last_extracted.txt`

---

## 💡 与Claude集成使用

### 方式1：自动提取后复制

```bash
# 运行工具
python3 ~/.claude/skills/xiaohongshu-content-generator/tools/fetch_xhs_auto.py <链接>

# 查看提取的内容
cat ~/.claude/skills/xiaohongshu-content-generator/data/last_extracted.txt

# 复制内容，然后对Claude说：
# "生成小红书内容：[粘贴内容]"
```

### 方式2：直接在Claude中使用

在Claude对话中输入：
```
读取文件 ~/.claude/skills/xiaohongshu-content-generator/data/last_extracted.txt
并生成小红书内容
```

---

## 🔧 高级配置

### 切换无头模式（不显示浏览器）

编辑 `fetch_xhs_auto.py`，找到：
```python
headless=False,  # 显示浏览器窗口
```

改为：
```python
headless=True,  # 后台运行，不显示窗口
```

### 重新登录

如果登录失效，删除保存的状态：
```bash
rm ~/.claude/skills/xiaohongshu-content-generator/data/xhs_auth.json
```

然后重新运行工具，会要求重新登录。

### 调整等待时间

如果网络慢，可以增加等待时间。编辑脚本中的：
```python
await asyncio.sleep(3)  # 改为更大的数字，如5或10
```

---

## 📂 文件位置

```
~/.claude/skills/xiaohongshu-content-generator/
├── tools/
│   └── fetch_xhs_auto.py          # 自动化脚本
└── data/
    ├── xhs_auth.json              # 保存的登录状态（自动生成）
    └── last_extracted.txt         # 最后提取的内容（自动生成）
```

---

## 🛠️ 故障排除

### 问题1：浏览器下载失败

```bash
# 重新安装浏览器
python3 -m playwright install chromium --force
```

### 问题2：登录后提取内容失败

可能原因：
- 页面加载慢，增加等待时间
- 小红书页面结构变化

解决：在浏览器打开后，手动等待内容完全加载再按回车。

### 问题3：登录状态失效

小红书的登录可能会过期，只需：
```bash
rm ~/.claude/skills/xiaohongshu-content-generator/data/xhs_auth.json
```

重新运行工具即可。

### 问题4：提取的内容不完整

尝试：
1. 在脚本中增加等待时间
2. 使用无头模式（headless=True）
3. 手动在浏览器中滚动页面，确保内容加载

---

## 🎬 完整使用示例

```bash
# 第一步：首次运行（需要登录）
$ python3 ~/.claude/skills/xiaohongshu-content-generator/tools/fetch_xhs_auto.py http://xhslink.com/o/2DIltcAJA2e

🚀 小红书自动化提取工具

🔗 目标链接：http://xhslink.com/o/2DIltcAJA2e

🔐 首次使用，需要登录小红书

📱 浏览器已打开，请按照以下步骤操作：

1️⃣  在浏览器中登录小红书
2️⃣  确认可以看到完整内容
3️⃣  返回终端，按回车键继续

👉 登录完成后，按回车键继续...

# [你在浏览器中登录，然后按回车]

🔗 正在访问：http://xhslink.com/o/2DIltcAJA2e
✅ 登录状态已保存

📝 提取内容中...

==================================================
📄 提取的内容
==================================================

【标题】
《吉赛尔》芭蕾舞剧第二幕赏析

【内容】
《吉赛尔》(Giselle)，浪漫主义芭蕾舞剧的代表作...
[完整内容]

==================================================

💾 内容已保存到：~/.claude/skills/xiaohongshu-content-generator/data/last_extracted.txt

✅ 提取成功！

# 第二步：使用Claude生成
现在打开Claude，说：
"读取文件 ~/.claude/skills/xiaohongshu-content-generator/data/last_extracted.txt
并生成小红书内容"
```

---

## 🌟 最佳实践

1. **首次使用建议在有头模式下**，确认登录成功
2. **后续使用可切换到无头模式**，提高效率
3. **定期清理保存的文件**，避免占用空间
4. **如遇到问题，查看完整的终端输出**，有详细的错误信息

---

## 🎯 下一步

浏览器下载完成后，立即运行：

```bash
python3 ~/.claude/skills/xiaohongshu-content-generator/tools/fetch_xhs_auto.py http://xhslink.com/o/2DIltcAJA2e
```

开始你的自动化之旅！🚀
