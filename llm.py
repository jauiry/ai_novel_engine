# LLM 调用模块
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="your-api-key-here",
    base_url="https://api.minimax.chat/v1"
)


def chat(prompt, model="MiniMax-M2.5", temperature=0.7):
    """
    调用 LLM 生成回复

    Args:
        prompt: 提示词
        model: 模型名称
        temperature: 温度参数

    Returns:
        AI 回复内容
    """
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    return completion.choices[0].message.content
