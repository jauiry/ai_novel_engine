# Editor Agent - 编辑 Agent
from llm import ask_llm


def edit_chapter(text):
    """
    润色小说

    Args:
        text: 原始文本

    Returns:
        润色后的文本
    """
    prompt = f"""
    润色小说：
    {text}
    让语言更流畅
    增加细节
    """

    return ask_llm(prompt)
