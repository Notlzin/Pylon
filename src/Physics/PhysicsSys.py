# PhysicsSys.py #
from src.PlayerSystem.component import Position, Velocity, Sprite

class Physics:
    def __init__(self, w, h):
        self.w = w # width #
        self.h = h # height #
        
    def update(self, entities):
        for entity in entities:
            pos = entity.getComponent(Position)
            vel = entity.getComponent(Velocity)
            spr = entity.getComponent(Sprite)
            if pos and vel and spr:
                # basic boundary collision system #
                if pos.x < 0 or pos.x + spr.surface.get_width() > self.w:
                    vel.dx *= -1 # horizontal bounce #
                if pos.y < 0 or pos.y + spr.surface.get_width() > self.h:
                    vel.dy *= -1 # vertical bounce #
                # applying velocity #
                pos.x += vel.dx
                pos.y += vel.dy
                # clamping to the screen limit #
                w, h = spr.surface.get_size()
                pos.x = max(0, min(pos.x, self.w - w))
                pos.y = max(0, min(pos.y, self.h - h))
