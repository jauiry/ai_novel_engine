# NPC Generator - NPC生成
import random


class NPC:

    def __init__(self, name, role, personality):

        self.name = name
        self.role = role
        self.personality = personality


def generate_npc(location):
    """当角色进入某个地方时，自动生成 NPC"""

    names = [
        "张老板",
        "李掌柜",
        "老陈",
        "神秘修士",
        "年轻弟子"
    ]

    roles = [
        "酒馆老板",
        "商人",
        "散修",
        "情报贩子",
        "宗门弟子"
    ]

    personalities = [
        "谨慎",
        "热情",
        "冷漠",
        "狡猾"
    ]

    name = random.choice(names)
    role = random.choice(roles)
    personality = random.choice(personalities)

    return NPC(name, role, personality)
