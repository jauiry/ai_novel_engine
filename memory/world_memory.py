# World Memory - 保存历史事件，记录世界变化


class WorldMemory:

    def __init__(self):

        self.events = []
        self.relationships = {}

    def add_event(self, event):

        self.events.append(event)

    def get_recent_events(self, n=5):

        return self.events[-n:]

    def add_relationship(self, char1, char2, relation):

        key = f"{char1}-{char2}"

        self.relationships[key] = relation

    def get_relationship(self, char1, char2):

        key = f"{char1}-{char2}"

        return self.relationships.get(key, "陌生")
