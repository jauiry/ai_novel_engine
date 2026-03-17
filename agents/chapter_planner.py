# Chapter Planner - 章节规划 Agent
from llm import ask_llm


def plan_chapter(context):
    """
    根据剧情规划下一章剧情

    Args:
        context: 剧情上下文

    Returns:
        章节规划
    """
    prompt = f"""
    根据剧情：
    {context}
    规划下一章剧情
    """

    return ask_llm(prompt)
