# Dialogue Writer - NPC + 角色 → 小说对话
from ai.dialogue_ai import generate_dialogue
from characters.npc_generator import generate_npc


def run_dialogue_scene(character, location):

    npc = generate_npc(location)

    dialogue = generate_dialogue(character, npc, location)

    scene = f"""
林凡在{location}遇到了{npc.role}【{npc.name}】。

{dialogue}
"""

    return scene
