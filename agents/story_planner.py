# Story Planner - 故事规划 Agent
from llm import ask_llm


def plan_story():
    """
    规划小说剧情：
    第一卷、第二卷、第三卷

    每卷包含：
    - 目标
    - 冲突
    - 高潮
    """
    prompt = """
    规划小说剧情：
    第一卷
    第二卷
    第三卷
    每卷包含：
    目标
    冲突
    高潮
    """

    story = ask_llm(prompt)

    with open("data/story.txt", "w", encoding="utf-8") as f:
        f.write(story)

    return story
