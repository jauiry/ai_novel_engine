# Chapter Store - 保存章节
import os


class ChapterStore:
    def __init__(self):
        os.makedirs("novel", exist_ok=True)

    def save(self, cid, text):
        """保存章节"""
        path = f"novel/chapter_{cid}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
