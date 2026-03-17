# Memory Agent - 记忆管理 Agent
from llm import chat as ask_llm


def summarize_events(events):
    """
    总结事件

    Args:
        events: 事件列表

    Returns:
        事件摘要
    """
    if not events:
        return ""

    events_text = "\n".join([f"- {e}" for e in events])

    prompt = f"""
请用50字以内总结以下事件：

{events_text}

只返回摘要。
"""

    result = chat(prompt, temperature=0.5)

    return result.strip()


def extract_memories(text):
    """
    从文本中提取关键记忆

    Args:
        text: 文本内容

    Returns:
        关键记忆列表
    """
    prompt = f"""
请从以下文本中提取关键信息作为记忆点：

{text}

提取以下类型的信息：
- 重要事件
- 角色关系变化
- 世界设定细节
- 关键物品/地点

以列表形式返回。
"""

    result = chat(prompt, temperature=0.5)

    return result


def retrieve_relevant_memory(query, memory_bank):
    """
    检索相关记忆

    Args:
        query: 查询内容
        memory_bank: 记忆库

    Returns:
        相关记忆
    """
    prompt = f"""
请从以下记忆库中找出与查询相关的内容。

查询：{query}

记忆库：
{memory_bank}

返回最相关的记忆。
"""

    result = chat(prompt, temperature=0.5)

    return result.strip()


def update_memory(old_memory, new_events):
    """
    更新记忆

    Args:
        old_memory: 旧记忆
        new_events: 新事件

    Returns:
        更新后的记忆
    """
    prompt = f"""
请根据新事件更新记忆。

旧记忆：
{old_memory}

新事件：
{new_events}

返回更新后的记忆。
"""

    result = chat(prompt, temperature=0.5)

    return result.strip()
