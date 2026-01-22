#!/usr/bin/env python3
"""
小红书浏览器辅助工具
打开浏览器并保持登录状态，方便手动复制内容
"""

import subprocess
import sys
import time

def open_with_chrome(url):
    """使用Chrome打开（保持用户登录状态）"""
    try:
        # macOS
        subprocess.run([
            'open', '-a', 'Google Chrome', url
        ])
        print(f"✅ 已在Chrome中打开：{url}")
        print("\n📝 请在浏览器中：")
        print("1. 登录小红书（如果未登录）")
        print("2. 查看完整内容")
        print("3. 复制文本内容")
        print("4. 返回终端粘贴给Claude\n")
        return True
    except Exception as e:
        print(f"❌ 打开Chrome失败: {e}")
        return False

def open_with_safari(url):
    """使用Safari打开"""
    try:
        subprocess.run(['open', '-a', 'Safari', url])
        print(f"✅ 已在Safari中打开：{url}")
        return True
    except Exception as e:
        print(f"❌ 打开Safari失败: {e}")
        return False

def open_with_default(url):
    """使用默认浏览器打开"""
    try:
        subprocess.run(['open', url])
        print(f"✅ 已在默认浏览器中打开：{url}")
        return True
    except Exception as e:
        print(f"❌ 打开浏览器失败: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("用法: python3 open_xhs.py <小红书链接>")
        print("\n示例:")
        print("python3 open_xhs.py http://xhslink.com/o/2DIltcAJA2e")
        sys.exit(1)

    url = sys.argv[1]

    print(f"🔗 准备打开小红书链接...\n")

    # 尝试不同浏览器
    if '--chrome' in sys.argv:
        open_with_chrome(url)
    elif '--safari' in sys.argv:
        open_with_safari(url)
    else:
        # 默认尝试Chrome（保留登录状态）
        if not open_with_chrome(url):
            open_with_default(url)

    print("\n💡 提示：")
    print("- 小红书需要登录才能查看完整内容")
    print("- 浏览器会保持你的登录状态")
    print("- 复制内容后，在Claude中输入：")
    print('  "生成小红书内容：[粘贴内容]"')

if __name__ == "__main__":
    main()
