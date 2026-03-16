# Chapter Writer - 事件转小说段落
from ai.minimax_api import ask_minimax


def write_scene(event):
    prompt = f"""
根据下面事件写一段小说场景。

事件:
{event.describe()}

要求:
100字左右
有环境描写
有动作
"""

    result = ask_minimax(prompt)

    return result.strip()
