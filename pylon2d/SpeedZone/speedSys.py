# speedSys.py #
from pylon2d.PlayerSystem.component import Position, Velocity
import pygame

class SpeedZoneSys:
    def __init__(self) -> None:
        self.color = (0,255,0)

    def update(self,entities,zones):
        screen = pygame.display.get_surface()
        for ent in entities:
            vel = ent.getComponent(Velocity)
            pos = ent.getComponent(Position)
            if not vel or not pos:
                continue # skip #

            # boost logic i guess #
            for zone in zones:
                if (zone.x <= pos.x <= zone.x + zone.w and
                    zone.y <= pos.y <= zone.y + zone.h):
                    vel.dx *= zone.boost
                    vel.dy *= zone.boost

        for zone in zones:
            zone.draw(screen)
