# World Builder - 世界构建 Agent
from llm import chat


def build_world(genre="修仙", setting=None):
    """
    构建小说世界

    Args:
        genre: 小说类型
        setting: 世界设定（可选）

    Returns:
        世界设定字典
    """
    prompt = f"""
你是世界构建专家。

请创建一个{genre}小说的世界设定。

包括：
1. 世界背景
2. 主要势力/门派
3. 地理区域
4. 修炼体系
5. 重要规则

请以JSON格式返回，包含以下字段：
{{
    "background": "世界背景描述",
    "factions": ["势力1", "势力2", ...],
    "regions": ["区域1", "区域2", ...],
    "cultivation_system": "修炼体系描述",
    "rules": ["规则1", "规则2", ...]
}}
"""

    result = chat(prompt)

    # 简单解析（实际可以用 JSON 解析）
    return result


def save_world(world_data):
    """保存世界设定到文件"""
    with open("data/world.txt", "w", encoding="utf-8") as f:
        f.write(str(world_data))
