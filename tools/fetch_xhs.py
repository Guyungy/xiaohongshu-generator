#!/usr/bin/env python3
"""
小红书内容获取工具
由于小红书的反爬虫机制，本工具提供辅助方法
"""

import sys
import json
from pathlib import Path


def fetch_from_clipboard():
    """从剪贴板读取内容"""
    try:
        import pyperclip
        content = pyperclip.paste()
        if content:
            print("✅ 已从剪贴板读取内容")
            return content
        else:
            print("❌ 剪贴板为空")
            return None
    except ImportError:
        print("⚠️  需要安装 pyperclip: pip install pyperclip")
        return None


def fetch_from_file(file_path):
    """从文件读取内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✅ 已从文件读取内容: {file_path}")
        return content
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return None


def interactive_input():
    """交互式输入"""
    print("\n请粘贴小红书内容（输入END结束）:")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        except EOFError:
            break

    content = '\n'.join(lines)
    if content:
        print("✅ 已接收内容")
        return content
    else:
        print("❌ 未接收到内容")
        return None


def save_content(content, output_file=None):
    """保存内容到文件"""
    if not output_file:
        output_file = "xhs_content.txt"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 内容已保存到: {output_file}")
        return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False


def main():
    """主函数"""
    print("🎯 小红书内容获取工具\n")

    if len(sys.argv) > 1:
        # 命令行参数
        if sys.argv[1] == '--clipboard':
            content = fetch_from_clipboard()
        elif sys.argv[1] == '--file':
            if len(sys.argv) > 2:
                content = fetch_from_file(sys.argv[2])
            else:
                print("❌ 请提供文件路径: --file <path>")
                return
        else:
            print("❌ 未知参数")
            print("用法:")
            print("  python fetch_xhs.py --clipboard    # 从剪贴板读取")
            print("  python fetch_xhs.py --file <path>  # 从文件读取")
            print("  python fetch_xhs.py                # 交互式输入")
            return
    else:
        # 交互式输入
        content = interactive_input()

    if content:
        # 可选：保存到文件
        save = input("\n是否保存到文件? (y/n): ").strip().lower()
        if save == 'y':
            output = input("文件名 (默认: xhs_content.txt): ").strip()
            save_content(content, output if output else None)

        print("\n" + "="*50)
        print("📝 获取的内容:")
        print("="*50)
        print(content[:500])  # 只显示前500字符
        if len(content) > 500:
            print("\n... (内容过长，已截断)")
        print("="*50)
    else:
        print("\n❌ 未能获取内容")


if __name__ == "__main__":
    main()
