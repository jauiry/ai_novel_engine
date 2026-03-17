# Critic Agent - 批评与检查 Agent
from llm import ask_llm


def review_chapter(text):
    """
    检查小说质量，如果有问题请改写

    Args:
        text: 小说文本

    Returns:
        审查后的文本
    """
    prompt = f"""
    检查小说质量：
    {text}
    如果有问题请改写
    """

    return ask_llm(prompt)
