# LLM 调用模块
import requests
from config import MODEL, TEMPERATURE


def chat(prompt, model=None, temperature=None):
    """
    调用 LLM 生成回复（使用 Ollama 本地模型）

    Args:
        prompt: 提示词
        model: 模型名称（默认读取 config.py）
        temperature: 温度参数（默认读取 config.py）

    Returns:
        AI 回复内容
    """
    model = model or MODEL
    temperature = temperature or TEMPERATURE

    url = "http://localhost:11434/api/generate"

    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }

    r = requests.post(url, json=data)
    return r.json()["response"]


# 别名
ask_llm = chat
