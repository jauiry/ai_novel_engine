# Writer Agent - 写作 Agent
from llm import ask_llm


def write_chapter(context):
    """
    参考设定写一章小说

    Args:
        context: 上下文/设定

    Returns:
        小说章节
    """
    prompt = f"""
    参考设定：
    {context}
    写一章小说：
    要求：
    2000字
    包含对话
    有冲突
    """

    return ask_llm(prompt)
