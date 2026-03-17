# World Builder - 世界构建 Agent
from llm import ask_llm


def build_world():
    """
    构建小说世界
    """
    prompt = """
    创建小说世界观：

    包括：
    世界名称
    修炼体系
    历史背景
    地理结构
    力量体系
    """

    world = ask_llm(prompt)

    with open("data/world.txt", "w", encoding="utf-8") as f:
        f.write(world)

    return world
