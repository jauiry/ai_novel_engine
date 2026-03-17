# AI Novel Engine - Main Entry
from agents.world_builder import build_world, save_world
from agents.character_builder import create_character
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
    world_data = build_world("修仙")
    print(world_data)
    save_world(world_data)

    # 2. 创建角色
    print("\n[2] 创建角色...")
    protagonist = create_character("林凡", "主角", "修仙")
    print(protagonist)

    # 3. 规划故事
    print("\n[3] 规划故事...")
    story_arc = plan_story(world_data, [protagonist], "修仙小说")
    print(story_arc)

    # 4. 写作章节
    print("\n[4] 写作章节...")
    store = ChapterStore("data")

    # 写3章
    for i in range(1, 4):
        print(f"\n--- 第 {i} 章 ---")

        # 规划章节
        chapter_plan = plan_chapter(story_arc, i)
        print(f"章节规划: {chapter_plan}")

        # 写作
        chapter_content = write_chapter(chapter_plan, world_data)
        print(chapter_content)

        # 保存
        store.save_chapter(i, chapter_content, {"title": f"第{i}章"})

    # 5. 保存完整小说
    print("\n[5] 保存小说...")
    store.save_to_file("data/story.txt")
    print("小说已保存到 data/story.txt")


if __name__ == "__main__":
    main()
