# Character Builder - 角色创建 Agent
from llm import chat


def create_character(name=None, role="主角", genre="修仙"):
    """
    创建小说角色

    Args:
        name: 角色名（可选）
        role: 角色类型（主角/配角/反派）
        genre: 小说类型

    Returns:
        角色设定字典
    """
    prompt = f"""
你是角色设计专家。

请为{genre}小说创建一个{role}角色。

请以JSON格式返回，包含以下字段：
{{
    "name": "角色名字",
    "age": 年龄,
    "personality": "性格特点",
    "background": "背景故事",
    "goals": ["目标1", "目标2"],
    "abilities": ["能力1", "能力2"],
    "relationships": {{"角色名": "关系描述"}}
}}
"""

    result = chat(prompt)

    return result


def create_npc(location, genre="修仙"):
    """
    创建NPC

    Args:
        location: 所在地点
        genre: 小说类型

    Returns:
        NPC 设定
    """
    prompt = f"""
你在创建{genre}小说的NPC。

地点：{location}

请随机创建一个NPC，包含：
- 名字
- 身份/职业
- 性格
- 与主角潜在的关系

返回JSON格式：
{{
    "name": "名字",
    "role": "身份",
    "personality": "性格",
    "potential_relationship": "潜在关系"
}}
"""

    result = chat(prompt)

    return result
