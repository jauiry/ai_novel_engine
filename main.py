# AI Novel Engine - Main Entry
from agents.world_builder import build_world
from agents.character_builder import build_characters
from agents.story_planner import plan_story
from agents.chapter_planner import plan_chapter
from agents.writer_agent import write_chapter
from storage.chapter_store import ChapterStore


def main():
    print("=" * 50)
    print("AI Novel Engine")
    print("=" * 50)

    # 1. 构建世界
    print("\n[1] 构建世界...")
    world_data = build_world()
    print(world_data)

    # 2. 创建角色
    print("\n[2] 创建角色...")
    characters = build_characters()
    print(characters)

    # 3. 规划故事
    print("\n[3] 规划故事...")
    story_arc = plan_story()
    print(story_arc)

    # 4. 写作章节
    print("\n[4] 写作章节...")
    store = ChapterStore()

    # 写3章
    for i in range(1, 4):
        print(f"\n--- 第 {i} 章 ---")

        # 规划章节
        chapter_plan = plan_chapter(story_arc)
        print(f"章节规划: {chapter_plan}")

        # 写作
        chapter_content = write_chapter(chapter_plan)
        print(chapter_content)

        # 保存
        store.save(i, chapter_content)

    print("\n小说已保存到 novel/ 目录")


if __name__ == "__main__":
    main()
