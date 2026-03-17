# Chapter Planner - 章节规划 Agent
from llm import chat


def plan_chapter(story_arc, chapter_num, previous_summary=""):
    """
    规划单个章节

    Args:
        story_arc: 故事弧线/大纲
        chapter_num: 章节编号
        previous_summary: 上一章摘要

    Returns:
        章节规划
    """
    prompt = f"""
你是章节规划专家。

故事大纲：
{story_arc}

上一章摘要：
{previous_summary}

请规划第{chapter_num}章：

返回JSON格式：
{{
    "title": "章节标题",
    "summary": "本章摘要（50字内）",
    "key_events": ["事件1", "事件2"],
    "pacing": "节奏描述",
    "goals": ["本章要达成的目标"]
}}
"""

    result = chat(prompt)

    return result


def outline_scenes(chapter_plan):
    """
    规划章节内的场景

    Args:
        chapter_plan: 章节规划

    Returns:
        场景列表
    """
    prompt = f"""
根据以下章节规划，列出本章的场景顺序：

{chapter_plan}

请列出场景顺序，每个场景包括：
- 场景描述
- 涉及角色
- 场景目的
"""

    result = chat(prompt)

    return result
