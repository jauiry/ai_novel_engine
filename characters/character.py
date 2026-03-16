from ai.decision_ai import decide_action_ai


class Character:

    def __init__(self, name, personality, goal, location):

        self.name = name
        self.personality = personality
        self.goal = goal
        self.location = location

    def decide_action(self, world, events):

        action = decide_action_ai(self, world, events)

        return action
