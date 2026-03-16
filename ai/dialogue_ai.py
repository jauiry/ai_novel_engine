# Dialogue AI - 对话生成
from ai.minimax_api import ask_minimax


def generate_dialogue(character, npc, location):
    """角色和NPC之间的对话生成"""

    prompt = f"""
你在写一部修仙小说。

地点:
{location}

角色1:
名字:{character.name}
性格:{character.personality}
目标:{character.goal}

角色2:
名字:{npc.name}
身份:{npc.role}
性格:{npc.personality}

写一段他们之间的对话。

要求:
5~8句
有剧情信息
对话格式:

林凡：......
张老板：......
"""

    result = ask_minimax(prompt)

    return result.strip()
