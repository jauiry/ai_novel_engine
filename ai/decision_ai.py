import re
from ai.minimax_api import ask_minimax


def build_prompt(character, world, events):
    """构建决策提示词"""

    # 角色信息
    prompt = f"""你是角色{character.name}的AI。请根据以下信息决定角色的行动。

## 角色信息
- 姓名: {character.name}
- 性格: {character.personality}
- 目标: {character.goal}
- 当前所在: {character.location}

## 世界状态
- 时间: 第{world.time}天
- 天气: {world.weather}

## 当前地点信息
"""

    # 添加地点信息
    location_info = world.get_location_info(character.location)
    if location_info:
        prompt += f"- 描述: {location_info.get('description', '')}\n"
        prompt += f"- 势力: {location_info.get('faction', '无')}\n"
        prompt += f"- 危险等级: {location_info.get('danger_level', 1)}\n"

    # 最近事件
    if events:
        prompt += "\n## 最近事件\n"
        for i, event in enumerate(events[-5:], 1):
            prompt += f"{i}. {event}\n"

    prompt += "\n请直接输出角色要做的行动（一句话描述）。"

    return prompt


def parse_action(result):
    """解析AI返回的行动"""

    # 移除markdown代码块
    result = re.sub(r"```[\s\S]*?```", "", result)
    result = re.sub(r"```", "", result)

    # 只保留最后一行
    lines = result.strip().split("\n")
    return lines[-1].strip()


def decide_action_ai(character, world, events):
    """AI决策主函数"""

    prompt = build_prompt(character, world, events)

    result = ask_minimax(prompt)

    action = parse_action(result)

    return action
