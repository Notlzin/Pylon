# AI behavior system #
import random
from pylon2d.PlayerSystem.component import Position, Velocity

class AI:
    def __init__(self, speed=3, change_interval=15):
        self.speed = speed
        self.dx = random.choice([-2,-1,0,1,2])
        self.dy = random.choice([-2,-1,0,1,2])
        self.timer = 0
        self.change_interval = change_interval

class AISys:
    def update(self, entities):
        for entity in entities:
            ai = entity.getComponent(AI)
            vel = entity.getComponent(Velocity)
            if ai and vel:
                ai.timer += 1
                # randomly changing directions every "change_intervals" frame #
                if ai.timer >= ai.change_interval:
                    ai.dx = random.choice([-2,-1,0,1,2])
                    ai.dy = random.choice([-2,-1,0,1,2])
                    ai.timer = 0
                # velocity setting #
                vel.dx = ai.dx * ai.speed
                vel.dy = ai.dy * ai.speed
