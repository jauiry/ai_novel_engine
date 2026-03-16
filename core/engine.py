# Engine - 游戏引擎核心
from core.event import Event
from core.world import World
from story.chapter_writer import write_scene
from memory.world_memory import WorldMemory


class Engine:

    def __init__(self, world, characters):

        self.world = world
        self.characters = characters
        self.events = []
        self.story = []
        self.memory = WorldMemory()

    def step(self):
        """执行一步"""

        # 每个角色执行行动
        for char in self.characters:

            # AI 决定行动
            action = char.decide_action(self.world, self.events[-5:])

            # 创建事件
            event = Event(char, action, char.location)

            # 记录到历史
            self.events.append(event)

            # 添加到记忆
            self.memory.add_event(event)

            # 写入小说
            scene = write_scene(event)
            self.story.append(scene)

            print(event.describe())
            print(scene)  # 打印AI生成的小说段落

    def run(self, steps):
        """运行指定步数"""

        for i in range(steps):

            print(f"\n===================")
            print("世界推进")
            print("===================")

            self.step()

    def get_story(self):
        """获取生成的小说"""
        return "\n\n".join(self.story)

    def save_story(self, filename):
        """保存小说到文件"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.get_story())
        print(f"小说已保存到: {filename}")
