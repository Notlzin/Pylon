# src/FPSS/fpsSystem.py #
import pygame

class FPSCounter:
    def __init__(self, screen, clock, font_s=24, color=(255,255,255), bg_color=(0,0,0)):
        self.screen = screen
        self.font = pygame.font.SysFont(None, font_s)
        self.color = color
        self.bg_color = bg_color
        self.clock = clock
        self.fps = 0
        
    def update(self, clock):
        # rough fps calculation #
        self.fps = int(clock.get_fps())
        
        # render the FPS #
        fps_txt = self.font.render(f"FPS: {int(self.fps)}", True, self.color)
        # drawing background rectangle #
        txt_rect = fps_txt.get_rect(topleft=(10,10))
        pygame.draw.rect(self.screen, self.bg_color, txt_rect.inflate(6,6))
        
        # blit the text #
        self.screen.blit(fps_txt, txt_rect)