#!/usr/bin/env python3
"""
小红书浏览器自动化工具 - Playwright版本
功能：
1. 首次运行：打开浏览器，让你手动登录，保存登录状态
2. 后续运行：自动使用登录状态，提取内容
"""

import asyncio
import json
import sys
from pathlib import Path
from playwright.async_api import async_playwright

# 配置
STORAGE_FILE = Path.home() / ".claude/skills/xiaohongshu-content-generator/data/xhs_auth.json"
STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

async def first_time_login(url):
    """首次登录：打开浏览器，让用户手动登录"""
    print("🔐 首次使用，需要登录小红书\n")

    async with async_playwright() as p:
        # 启动有头浏览器（可以看到界面）
        browser = await p.chromium.launch(
            headless=False,  # 显示浏览器窗口
            args=['--start-maximized']
        )

        # 创建上下文
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )

        page = await context.new_page()

        print("📱 浏览器已打开，请按照以下步骤操作：\n")
        print("1️⃣  在浏览器中登录小红书")
        print("2️⃣  确认可以看到完整内容")
        print("3️⃣  等待60秒后自动继续...\n")

        # 打开小红书首页（让用户先登录）
        await page.goto('https://www.xiaohongshu.com/')

        # 等待用户登录（自动等待60秒）
        print("⏱️  等待60秒，请在浏览器中完成登录...")
        for i in range(60, 0, -10):
            print(f"   剩余 {i} 秒...")
            await asyncio.sleep(10)
        print("✅ 等待完成，继续执行...\n")

        # 现在访问目标链接
        print(f"\n🔗 正在访问：{url}")
        try:
            await page.goto(url, wait_until='networkidle', timeout=30000)
        except Exception as e:
            print(f"⚠️  访问链接超时，尝试继续...")
            await page.goto(url, timeout=60000)

        # 等待页面加载
        await asyncio.sleep(3)

        # 保存登录状态
        storage = await context.storage_state()
        with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
            json.dump(storage, f, ensure_ascii=False, indent=2)
        print(f"✅ 登录状态已保存到：{STORAGE_FILE}\n")

        # 提取内容
        content = await extract_content(page)

        print("\n⏱️  5秒后自动关闭浏览器...")
        await asyncio.sleep(5)
        await browser.close()

        return content


async def extract_with_saved_state(url):
    """使用保存的登录状态访问"""
    print("🔄 使用已保存的登录状态...\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,  # 可以改为True实现无头模式
            args=['--start-maximized']
        )

        # 使用保存的状态创建上下文
        context = await browser.new_context(
            storage_state=str(STORAGE_FILE),
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )

        page = await context.new_page()

        print(f"🔗 正在访问：{url}")
        try:
            await page.goto(url, wait_until='networkidle', timeout=30000)
        except Exception as e:
            print(f"⚠️  访问超时，尝试继续...")
            await page.goto(url, timeout=60000)

        # 等待内容加载
        await asyncio.sleep(3)

        # 提取内容
        content = await extract_content(page)

        print("\n💡 浏览器将在5秒后关闭...")
        await asyncio.sleep(5)
        await browser.close()

        return content


async def extract_content(page):
    """提取页面内容"""
    print("\n📝 提取内容中...\n")

    try:
        # 等待主要内容加载
        await page.wait_for_selector('body', timeout=10000)

        # 尝试多种选择器提取内容
        content_data = {
            'title': '',
            'content': '',
            'author': '',
            'tags': []
        }

        # 提取标题
        try:
            title_selectors = [
                '#detail-title',
                '.title',
                'h1',
                '[class*="title"]'
            ]
            for selector in title_selectors:
                element = await page.query_selector(selector)
                if element:
                    content_data['title'] = await element.inner_text()
                    break
        except:
            pass

        # 提取正文内容
        try:
            content_selectors = [
                '#detail-desc',
                '.desc',
                '.content',
                '[class*="note-text"]',
                '[class*="content"]'
            ]
            for selector in content_selectors:
                element = await page.query_selector(selector)
                if element:
                    content_data['content'] = await element.inner_text()
                    break
        except:
            pass

        # 如果上述方法都失败，提取整个body
        if not content_data['content']:
            body_text = await page.evaluate('() => document.body.innerText')
            content_data['content'] = body_text[:2000]  # 限制长度

        # 提取作者
        try:
            author_selectors = [
                '.author-name',
                '.username',
                '[class*="author"]'
            ]
            for selector in author_selectors:
                element = await page.query_selector(selector)
                if element:
                    content_data['author'] = await element.inner_text()
                    break
        except:
            pass

        # 提取标签
        try:
            tags = await page.query_selector_all('.tag, [class*="tag"]')
            for tag in tags[:10]:  # 最多10个标签
                tag_text = await tag.inner_text()
                if tag_text:
                    content_data['tags'].append(tag_text.strip())
        except:
            pass

        # 格式化输出
        result = "=" * 50 + "\n"
        result += "📄 提取的内容\n"
        result += "=" * 50 + "\n\n"

        if content_data['title']:
            result += f"【标题】\n{content_data['title']}\n\n"

        if content_data['author']:
            result += f"【作者】\n{content_data['author']}\n\n"

        if content_data['content']:
            result += f"【内容】\n{content_data['content']}\n\n"

        if content_data['tags']:
            result += f"【标签】\n{', '.join(content_data['tags'])}\n\n"

        result += "=" * 50

        print(result)

        # 保存到文件
        output_file = Path.home() / ".claude/skills/xiaohongshu-content-generator/data/last_extracted.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\n💾 内容已保存到：{output_file}")

        return result

    except Exception as e:
        print(f"❌ 提取内容失败：{e}")
        return None


async def main(url):
    """主函数"""
    # 检查是否已有保存的登录状态
    if STORAGE_FILE.exists():
        try:
            content = await extract_with_saved_state(url)
        except Exception as e:
            print(f"\n⚠️  使用保存的状态失败：{e}")
            print("🔄 尝试重新登录...\n")
            content = await first_time_login(url)
    else:
        content = await first_time_login(url)

    return content


def run(url):
    """运行异步主函数"""
    return asyncio.run(main(url))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 fetch_xhs_auto.py <小红书链接>")
        print("\n示例:")
        print("python3 fetch_xhs_auto.py http://xhslink.com/o/2DIltcAJA2e")
        sys.exit(1)

    url = sys.argv[1]

    print("🚀 小红书自动化提取工具\n")
    print(f"🔗 目标链接：{url}\n")

    try:
        content = run(url)
        if content:
            print("\n✅ 提取成功！")
            print("\n💡 你可以直接将提取的内容复制给Claude：")
            print('   "生成小红书内容：[粘贴内容]"')
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断")
    except Exception as e:
        print(f"\n❌ 错误：{e}")
        import traceback
        traceback.print_exc()
