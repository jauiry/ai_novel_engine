# Consistency Agent - 一致性检查 Agent
from llm import ask_llm


def check_consistency(text):
    """
    检查小说一致性

    Args:
        text: 小说文本

    Returns:
        一致性检查结果
    """
    prompt = f"""
    检查小说一致性：
    {text}
    是否有角色不符或情节矛盾？
    """

    return ask_llm(prompt)
