class Event:

    def __init__(self, actor, action, location):

        self.actor = actor
        self.action = action
        self.location = location

    def describe(self):
        return f"{self.actor.name} 在 {self.location} {self.action}"
