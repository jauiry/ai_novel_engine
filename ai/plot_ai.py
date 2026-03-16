# Plot AI - 剧情系统
from ai.minimax_api import ask_minimax


def generate_plot(world, recent_events):
    """根据世界状态生成剧情"""

    event_text = ""
    for e in recent_events:
        event_text += f"- {e.describe()}\n"

    prompt = f"""
你是小说剧情设计师。

当前世界：

地点：
{",".join(world.towns.keys())}

势力：
{",".join(world.factions.keys())}

最近发生的事情：
{event_text}

请生成一个新的剧情事件。

例如：
青云宗失踪事件
黑风山妖兽暴动
血刀门阴谋

只返回一个剧情标题。
"""

    result = ask_minimax(prompt)

    return result.strip()
