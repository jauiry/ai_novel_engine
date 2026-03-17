# Editor Agent - 编辑 Agent
from llm import chat


def edit_chapter(chapter_text, standards=None):
    """
    编辑章节

    Args:
        chapter_text: 章节内容
        standards: 编辑标准（可选）

    Returns:
        编辑后的内容
    """
    prompt = f"""
你是编辑专家。

请对以下章节进行编辑：

{chapter_text}

编辑要求：
- 改善语言表达
- 调整节奏
- 增强可读性
- 保持作者风格

直接返回编辑后的内容。
"""

    result = chat(prompt, temperature=0.5)

    return result.strip()


def polish_prose(text):
    """
    润色文笔

    Args:
        text: 原始文本

    Returns:
        润色后的文本
    """
    prompt = f"""
请润色以下文字，使其更加优美：

{text}

只返回润色后的内容。
"""

    result = chat(prompt, temperature=0.5)

    return result.strip()
