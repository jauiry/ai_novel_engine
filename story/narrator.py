def build_story_prompt(events):

    text = "根据以下事件写一段小说：\n\n"

    for e in events:
        text += f"- {e.describe()}\n"

    text += "\n请写成一段有画面感的小说。"

    return text