# Story Planner - 故事规划 Agent
from llm import chat


def plan_story(world_data, characters, story_type="修仙小说"):
    """
    规划整体故事线

    Args:
        world_data: 世界设定
        characters: 角色列表
        story_type: 故事类型

    Returns:
        故事大纲
    """
    characters_text = "\n".join([f"- {c}" for c in characters])

    prompt = f"""
你是故事规划专家。

请为{story_type}规划整体故事线。

世界设定：
{world_data}

角色列表：
{characters_text}

请规划：
1. 主线剧情
2. 关键转折点（3-5个）
3. 高潮部分
4. 结局方向

返回JSON格式：
{{
    "main_plot": "主线剧情描述",
    "turning_points": ["转折点1", "转折点2", ...],
    "climax": "高潮描述",
    "ending": "结局方向"
}}
"""

    result = chat(prompt)

    return result


def generate_plot_point(world_data, recent_events):
    """
    生成新的剧情点

    Args:
        world_data: 世界设定
        recent_events: 最近发生的事件

    Returns:
        新的剧情点
    """
    events_text = "\n".join([f"- {e}" for e in recent_events])

    prompt = f"""
你是剧情设计师。

当前世界设定：
{world_data}

最近发生的事件：
{events_text}

请生成一个新的剧情事件/冲突。

要求：
- 与已有剧情有关联
- 能推动故事发展
- 有戏剧性

直接返回一个剧情事件描述。
"""

    result = chat(prompt)

    return result.strip()
