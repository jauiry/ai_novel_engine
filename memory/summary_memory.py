# Summary Memory - 摘要记忆


class SummaryMemory:
    """
    摘要记忆系统
    用于存储和管理长篇内容的摘要
    """

    def __init__(self):
        self.chapters = []  # 章节摘要
        self.events = []    # 事件摘要
        self.character_states = {}  # 角色状态

    def add_chapter_summary(self, chapter_num, summary):
        """
        添加章节摘要

        Args:
            chapter_num: 章节编号
            summary: 章节摘要
        """
        self.chapters.append({
            "num": chapter_num,
            "summary": summary
        })

    def add_event_summary(self, event):
        """
        添加事件摘要

        Args:
            event: 事件描述
        """
        self.events.append(event)

    def update_character_state(self, character_name, state):
        """
        更新角色状态

        Args:
            character_name: 角色名
            state: 状态描述
        """
        self.character_states[character_name] = state

    def get_character_state(self, character_name):
        """
        获取角色状态

        Args:
            character_name: 角色名

        Returns:
            角色状态
        """
        return self.character_states.get(character_name, "")

    def get_recent_events(self, n=5):
        """
        获取最近事件

        Args:
            n: 数量

        Returns:
            最近事件列表
        """
        return self.events[-n:]

    def get_chapter_summary(self, chapter_num):
        """
        获取章节摘要

        Args:
            chapter_num: 章节编号

        Returns:
            章节摘要
        """
        for c in self.chapters:
            if c["num"] == chapter_num:
                return c["summary"]
        return ""

    def get_all_summaries(self):
        """获取所有摘要"""
        return {
            "chapters": self.chapters,
            "events": self.events,
            "characters": self.character_states
        }

    def clear(self):
        """清空记忆"""
        self.chapters = []
        self.events = []
        self.character_states = {}
