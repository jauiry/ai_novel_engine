# Story AI - 小说生成
from ai.minimax_api import ask_minimax


def write_story(prompt):
    """通用小说写作"""
    full_prompt = f"""你是一个玄幻小说作家。请根据以下信息写小说片段：

{prompt}

要求：
- 画面感强
- 细节丰富
- 符合玄幻风格
- 100-200字
"""
    return ask_minimax(full_prompt)


def write_scene(event):
    """根据事件写场景"""
    prompt = f"""根据事件写小说段落：

{event.describe()}
"""
    return write_story(prompt)


def write_dialogue(character1, character2, content):
    """写对话"""
    prompt = f"""写一段{character1.name}和{character2.name}的对话：
    场景: {character1.location}
    内容: {content}
    """
    return write_story(prompt)


def expand_event(event):
    """扩展事件为完整场景"""
    prompt = f"""将以下事件扩展为一个详细的场景描写（200-300字）：

{event.describe()}
"""
    return write_story(prompt)
