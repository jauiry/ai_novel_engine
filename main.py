from core.engine import Engine
from core.world import World
from characters.character import Character


world = World()

linfan = Character(
    name="林凡",
    personality="冷静谨慎",
    goal="成为最强修士",
    location="青云城"
)

engine = Engine(world, [linfan])


for i in range(3):

    print("\n===================")
    print("世界推进")
    print("===================")

    engine.step()
