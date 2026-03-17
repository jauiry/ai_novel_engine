# Character Builder - 角色创建 Agent
from llm import ask_llm


def build_characters():
    """
    生成小说角色：
    主角、反派、导师、伙伴

    每个角色包含：
    - 姓名
    - 性格
    - 能力
    - 目标
    - 背景
    """
    prompt = """
    生成小说角色：
    主角
    反派
    导师
    伙伴
    每个角色包含：
    姓名
    性格
    能力
    目标
    背景
    """

    chars = ask_llm(prompt)

    with open("data/characters.txt", "w", encoding="utf-8") as f:
        f.write(chars)

    return chars
