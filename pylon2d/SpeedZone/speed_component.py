# speed_component.py #
import pygame

class SpeedZone:
    def __init__(self,x,y,w,h,boost=2.5, color=(0,255,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.boost = boost
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h),2)
