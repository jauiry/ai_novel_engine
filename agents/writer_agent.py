# Writer Agent - 写作 Agent
from llm import chat


def write_scene(setting, characters, action, style="修仙小说"):
    """
    写作场景

    Args:
        setting: 场景设定（地点、环境）
        characters: 涉及的角色
        action: 发生的动作/事件
        style: 小说风格

    Returns:
        小说段落
    """
    prompt = f"""
请根据以下信息写一段{style}风格的场景。

场景设定：
{setting}

涉及角色：
{characters}

事件/动作：
{action}

要求：
- 100-200字
- 有环境描写
- 有动作描写
- 符合{style}风格
"""

    result = chat(prompt, temperature=0.8)

    return result.strip()


def write_dialogue(character1, character2, context, purpose):
    """
    写作对话

    Args:
        character1: 角色1信息
        character2: 角色2信息
        context: 对话背景
        purpose: 对话目的

    Returns:
        对话内容
    """
    prompt = f"""
请写一段对话。

角色1：{character1}
角色2：{character2}

背景：{context}
目的：{purpose}

要求：
- 符合角色性格
- 推动剧情
- 有信息量

对话格式：
角色1：xxx
角色2：xxx
"""

    result = chat(prompt, temperature=0.7)

    return result.strip()


def write_chapter(chapter_plan, world_data):
    """
    写作完整章节

    Args:
        chapter_plan: 章节规划
        world_data: 世界设定

    Returns:
        完整章节内容
    """
    prompt = f"""
请根据以下规划写一个完整的章节。

章节规划：
{chapter_plan}

世界设定：
{world_data}

要求：
- 1000-2000字
- 情节丰富
- 描写细腻
- 符合小说风格
"""

    result = chat(prompt, temperature=0.8)

    return result.strip()
