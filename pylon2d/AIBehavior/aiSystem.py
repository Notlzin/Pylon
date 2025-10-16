# aiSystem.py #
# AI Behavioral System and also GPT-5mini creation, but there are slight changes from the original tho #
import random
from pylon2d.PlayerSystem.component import Velocity

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

                # change direction every interval, but with a little bias #
                if ai.timer >= ai.change_interval:
                    # biasing: prefer current direction, but still allow jumps #
                    def biased_choice(curr):
                        options = [-2,-1,0,1,2]
                        weights = [1, 1, 2, 1, 1]  # 0 (stay) slightly favored #
                        return random.choices(options, weights=weights)[0]

                    ai.dx = biased_choice(ai.dx)
                    ai.dy = biased_choice(ai.dy)

                    ai.timer = 0
                    ai.change_interval = random.randint(10, 20)  # add slight randomness #

                # applying velocity #
                vel.dx = ai.dx * ai.speed
                vel.dy = ai.dy * ai.speed
