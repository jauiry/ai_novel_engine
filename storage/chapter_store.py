# Chapter Store - 章节存储


class ChapterStore:
    """
    章节存储系统
    用于保存和管理小说章节
    """

    def __init__(self, base_path="data"):
        self.base_path = base_path
        self.chapters = {}

    def save_chapter(self, chapter_num, content, metadata=None):
        """
        保存章节

        Args:
            chapter_num: 章节编号
            content: 章节内容
            metadata: 元数据（标题、日期等）
        """
        self.chapters[chapter_num] = {
            "content": content,
            "metadata": metadata or {}
        }

        # 同时保存到文件
        filename = f"{self.base_path}/chapter_{chapter_num}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    def get_chapter(self, chapter_num):
        """
        获取章节

        Args:
            chapter_num: 章节编号

        Returns:
            章节内容
        """
        if chapter_num in self.chapters:
            return self.chapters[chapter_num]

        # 从文件读取
        filename = f"{self.base_path}/chapter_{chapter_num}.txt"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                self.chapters[chapter_num] = {"content": content}
                return {"content": content}
        except FileNotFoundError:
            return None

    def get_all_chapters(self):
        """获取所有章节"""
        return self.chapters

    def get_full_story(self):
        """
        获取完整故事

        Returns:
            完整小说文本
        """
        sorted_chapters = sorted(self.chapters.keys())
        parts = []

        for num in sorted_chapters:
            parts.append(self.chapters[num]["content"])

        return "\n\n".join(parts)

    def save_to_file(self, filename):
        """
        保存完整小说到文件

        Args:
            filename: 文件名
        """
        story = self.get_full_story()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(story)

    def delete_chapter(self, chapter_num):
        """
        删除章节

        Args:
            chapter_num: 章节编号
        """
        if chapter_num in self.chapters:
            del self.chapters[chapter_num]
