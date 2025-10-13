# src/InputSystem/playerMovement.py #
import pygame
from pylon2d.PlayerSystem.component import Position, Velocity, Sprite

# setting up controls #
class Controller:
    def __init__(self, speed=6, acceleration=0.5):
        self.speed = speed
        self.accel = acceleration

    def update(self, entities):
        key = pygame.key.get_pressed()
        for entity in entities:
            pos = entity.getComponent(Position)
            vel = entity.getComponent(Velocity)
            spr = entity.getComponent(Sprite)
            if vel and pos and spr:
                target_dx, target_dy = 0,0
                if key[pygame.K_LEFT] or key[pygame.K_a]:
                   vel.dx -= self.speed
                if key[pygame.K_RIGHT] or key[pygame.K_d]:
                    vel.dx += self.speed
                if key[pygame.K_UP] or key[pygame.K_w]:
                    vel.dy -= self.speed
                if key[pygame.K_DOWN] or key[pygame.K_s]:
                    vel.dy += self.speed

                # acceleration / deceleration #
                vel.dx += (target_dx - vel.dx) * self.accel
                vel.dy += (target_dy - vel.dy) * self.accel
