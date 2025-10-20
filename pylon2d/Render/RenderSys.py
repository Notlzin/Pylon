# RenderSys.py #
from pylon2d.PlayerSystem.component import Position, Sprite
class Render:
    def __init__(self, screen, clearColor=(0,0,0)):
        self.screen = screen
        self.clearColor = clearColor

    def update(self, entities, camera=None):
        self.screen.fill(self.clearColor)
        for ent in entities:
            pos = ent.getComponent(Position)
            spr = ent.getComponent(Sprite)
            if pos and spr:
                self.screen.blit(spr.surface, (pos.x, pos.y))
