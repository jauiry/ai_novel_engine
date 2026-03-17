# Critic Agent - 批评/反馈 Agent
from llm import chat


def critique_chapter(chapter_text, criteria=None):
    """
    批评/评审章节

    Args:
        chapter_text: 章节内容
        criteria: 评审标准（可选）

    Returns:
        评审意见
    """
    prompt = f"""
你是文学批评专家。

请评审以下章节：

{chapter_text}

评审维度：
- 情节合理性
- 人物塑造
- 文笔水平
- 节奏把控
- 创新点

请以JSON格式返回：
{{
    "overall_score": 评分0-10,
    "strengths": ["优点1", "优点2"],
    "weaknesses": ["缺点1", "缺点2"],
    "suggestions": ["建议1", "建议2"]
}}
"""

    result = chat(prompt, temperature=0.3)

    return result


def suggest_improvements(critique):
    """
    根据评审意见建议改进

    Args:
        critique: 评审意见

    Returns:
        改进建议
    """
    prompt = f"""
基于以下评审意见，请给出具体的改进方案：

{critique}

请列出具体可执行的改进步骤。
"""

    result = chat(prompt)

    return result.strip()
