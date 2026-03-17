# Vector Memory - 向量记忆系统
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


class VectorMemory:
    def __init__(self):
        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add(self, text):
        """添加记忆"""
        vec = model.encode(text)
        self.index.add(np.array([vec]).astype("float32"))
        self.texts.append(text)

    def search(self, query, k=5):
        """搜索相关记忆"""
        vec = model.encode(query)
        D, I = self.index.search(np.array([vec]).astype("float32"), k)
        return [self.texts[i] for i in I[0]]
