# AI Novel Engine Configuration

# 模型配置
MODEL = "qwen2:7b"
TEMPERATURE = 0.7

# 章节配置
TOTAL_CHAPTERS = 1000
WORDS_PER_CHAPTER = 2000

# 记忆配置
VECTOR_TOP_K = 5
SUMMARY_INTERVAL = 10

# API 配置（备用）
API_CONFIG = {
    "provider": "minimax",
    "api_key": "your-api-key-here",
    "base_url": "https://api.minimax.chat/v1",
    "model": "MiniMax-M2.5"
}

# 世界设定
WORLD_CONFIG = {
    "locations": [
        "青云城",
        "黑风山",
        "落日森林"
    ]
}
