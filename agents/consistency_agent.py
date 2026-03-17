# Consistency Agent - 一致性检查 Agent
from llm import chat


def check_consistency(new_text, world_data, character_profiles, history):
    """
    检查新内容的一致性

    Args:
        new_text: 新写的文本
        world_data: 世界设定
        character_profiles: 角色档案
        history: 历史内容

    Returns:
        一致性检查结果
    """
    prompt = f"""
你是一致性检查专家。

请检查以下新写的内容是否与已有设定一致。

世界设定：
{world_data}

角色设定：
{character_profiles}

历史内容摘要：
{history}

新写内容：
{new_text}

请检查：
1. 世界观是否一致
2. 角色性格/能力是否一致
3. 剧情逻辑是否连贯
4. 是否有前后矛盾

返回JSON格式：
{{
    "is_consistent": true/false,
    "issues": ["问题1", "问题2"],
    "suggestions": ["修改建议1", "修改建议2"]
}}
"""

    result = chat(prompt, temperature=0.3)

    return result


def fix_inconsistencies(text, issues):
    """
    修复不一致的地方

    Args:
        text: 有问题的文本
        issues: 发现的问题

    Returns:
        修复后的文本
    """
    prompt = f"""
请根据以下问题修复文本：

发现问题：
{issues}

原文：
{text}

请直接返回修复后的内容。
"""

    result = chat(prompt, temperature=0.5)

    return result.strip()
