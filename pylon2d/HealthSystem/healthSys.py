# pylon2d/healthSys.py #
import pygame
from pylon2d.PlayerSystem.component import Health, Position, Sprite

class HealthBar:
    """Component to link a health bar entity to its owner.
        note: GPT-5 multi-line comment bruh
    """
    def __init__(self, owner_entity):
        self.owner = owner_entity  # the player or AI entity this bar belongs to #

class healthSys:
    def __init__(self, screen):
        self.screen = screen

    def update(self, entities):
        for ent in entities:
            # check if this entity is a health bar #
            hb = ent.getComponent(HealthBar)
            spr = ent.getComponent(Sprite)
            pos = ent.getComponent(Position)
            if not hb or not spr or not pos:
                continue

            # get owners position and health #
            owner = hb.owner
            owner_pos = owner.getComponent(Position)
            owner_spr = owner.getComponent(Sprite)
            owner_hp = owner.getComponent(Health)

            if not owner_pos or not owner_spr or not owner_hp:
                continue

            # position the health bar above the owner #
            pos.x = owner_pos.x
            pos.y = owner_pos.y - 10  # 10 pixels above ofc GPT-5mini #

            # calculate health percentage #
            healthPCT = max(0, min(1, owner_hp.current / owner_hp.max))
            bar_width = spr.surface.get_width()
            bar_height = spr.surface.get_height()
            green_width = int(bar_width * healthPCT)

            # draw red background for health bar #
            pygame.draw.rect(self.screen, (255, 0, 0), (pos.x, pos.y, bar_width, bar_height))
            # draw green foreground
            if green_width > 0:
                pygame.draw.rect(self.screen, (0, 255, 0), (pos.x, pos.y, green_width, bar_height))
