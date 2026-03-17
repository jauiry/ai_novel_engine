# Planner Agent - 规划 Agent
from llm import chat as ask_llm


def plan_novel(genre, premise, target_length="中篇小说"):
    """
    规划整本小说

    Args:
        genre: 小说类型
        premise: 小说前提/创意
        target_length: 目标长度

    Returns:
        小说规划
    """
    prompt = f"""
你是小说规划专家。

请为以下创意规划一本{genre}小说：

创意/前提：{premise}

目标长度：{target_length}

请提供：
1. 故事核心概念
2. 主线剧情
3. 角色介绍
4. 章节规划（5-10章）
5. 高潮和结局

返回详细的小说规划。
"""

    result = chat(prompt, temperature=0.7)

    return result


def plan_next_step(current_state, story_arc):
    """
    规划下一步

    Args:
        current_state: 当前状态
        story_arc: 故事弧线

    Returns:
        下一步规划
    """
    prompt = f"""
你是故事规划专家。

当前状态：
{current_state}

故事弧线：
{story_arc}

请规划下一步：
- 接下来应该发生什么
- 如何推进剧情
- 可能的转折

返回你的规划。
"""

    result = chat(prompt, temperature=0.7)

    return result.strip()
