# src/FPSS/fpsSystem.py #
import pygame
from collections import deque

class FPSCounter:
    def __init__(self, screen, clock, font_s=24, color=(255,255,255), bg_color=(0,0,0), smoothing=25):
        self.screen = screen
        self.font = pygame.font.SysFont(None, font_s)
        self.color = color
        self.bg_color = bg_color
        self.clock = clock
        self.smoothing = smoothing
        self.fps_hist = deque(maxlen=smoothing)
        self.fps = 0
        self.pos = (10,10)
        self.padding = 4

    def update(self):
        # record current frame FPS
        self.fps_hist.append(self.clock.get_fps())
        # rolling average for smooth display
        self.fps = sum(self.fps_hist) / len(self.fps_hist) if self.fps_hist else 0
        # render FPS text on screen #
        fps_txt = self.font.render(f"FPS: {int(self.fps)}", True, self.color)
        txt_rect = fps_txt.get_rect(topleft=self.pos)
        # draw background rectangle #
        pygame.draw.rect(self.screen, self.bg_color, txt_rect.inflate(self.padding, self.padding))
        # blit text
        self.screen.blit(fps_txt, txt_rect)
    # optional [yes GPT-5mini thing]: let user move the FPS display #
    def set_position(self, x, y):
        self.pos = (x, y)
