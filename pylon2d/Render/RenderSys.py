# RenderSys.py #
from pylon2d.PlayerSystem.component import Position, Sprite
import pygame

class Render:
    def __init__(self, screen):
        self.screen = screen

    def update(self, entities):
        self.screen.fill((0,0,0))
        for entity in entities:
            pos = entity.getComponent(Position)
            spr = entity.getComponent(Sprite)
            if pos and spr:
                self.screen.blit(spr.surface, (pos.x, pos.y))
        pygame.display.flip()
