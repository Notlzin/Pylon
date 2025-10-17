# gameEngine.py aka the game engine and also some comments are made by GPT (the multiline ones) #
import pygame
from pylon2d.MovementSystem.movement import MovementSys
from pylon2d.Physics.PhysicsSys import Physics
from pylon2d.Render.RenderSys import Render
from pylon2d.InputSystem.playerMovement import Controller
from pylon2d.AIBehavior.aiSystem import AISys
from pylon2d.FPSS.fpsSystem import FPSCounter
from pylon2d.SpeedZone import SpeedZoneSys, SpeedZone
from typing import List, Optional

# game engine class #
class gEngine:
    def __init__(self, w=800, h=600, fps=75):
        pygame.init()
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("My 2D Engine [and also GPT's]")

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.entities = []
        self.clock = pygame.time.Clock() # note: this is for the FPS text rendering #

        # systems #
        self.movement_sys = MovementSys()
        self.physics_sys = Physics(w, h)
        self.render_sys = Render(screen=self.screen)
        self.ai_sys = AISys()
        self.control_sys = Controller()
        self.fps_count = FPSCounter(self.screen, self.clock)
        # self.health_sys = healthSys(self.screen) experimental #
        self.speed_zones: List[SpeedZone] = []
        self.speed_sys: Optional[SpeedZoneSys] = None
        # -------------------------------------#

    def addEntity(self, entity):
        """Adding an entity [with components] to the engine."""
        self.entities.append(entity)

    def handle_events(self):
        """Handling pygame events like quitting."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def runner(self):
        """Main game loop."""
        while self.running:
            self.handle_events()

            # update systems #
            self.control_sys.update(self.entities)
            self.ai_sys.update(self.entities)
            self.movement_sys.update(self.entities)
            self.physics_sys.update(self.entities)
            if self.speed_sys is not None:
                self.speed_sys.update(self.entities, self.speed_zones)
            self.render_sys.update(self.entities)
            # self.health_sys.update(self.entities) this too #
            self.fps_count.update()
            pygame.display.flip()
            self.clock.tick(self.fps)
            # systems update #

        pygame.quit()
