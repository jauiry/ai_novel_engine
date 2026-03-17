# Vector Memory - 向量记忆（需要 faiss）
# 如果没有 faiss，使用简单的文本存储


class VectorMemory:
    """
    向量记忆系统
    用于存储和检索重要信息
    """

    def __init__(self):
        self.memories = []
        self.vectors = None

        try:
            import faiss
            self.has_faiss = True
            self.dimension = 768  # embedding 维度
            self.vectors = faiss.IndexFlatL2(self.dimension)
        except ImportError:
            self.has_faiss = False
            print("Warning: faiss not installed, using simple text storage")

    def add(self, text, metadata=None):
        """
        添加记忆

        Args:
            text: 记忆文本
            metadata: 元数据（可选）
        """
        memory = {
            "text": text,
            "metadata": metadata or {}
        }
        self.memories.append(memory)

        # TODO: 如果有 faiss，添加向量

    def search(self, query, top_k=5):
        """
        搜索相关记忆

        Args:
            query: 查询文本
            top_k: 返回数量

        Returns:
            相关记忆列表
        """
        # 简单实现：文本包含查询词即匹配
        results = []
        for m in self.memories:
            if query in m["text"]:
                results.append(m)

        return results[:top_k]

    def get_all(self):
        """获取所有记忆"""
        return self.memories

    def clear(self):
        """清空记忆"""
        self.memories = []
