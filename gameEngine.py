# gameEngine.py aka the game engine #
import pygame
from src.MovementSystem.movement import MovementSys
from src.Physics.PhysicsSys import Physics
from src.Render.RenderSys import Render
from src.InputSystem.playerMovement import Controller
from src.AIBehavior.aiSystem import AISys
from src.FPSS.fpsSystem import FPSCounter

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
            self.render_sys.update(self.entities)
            self.fps_count.update(self.clock)
            pygame.display.flip()
            self.clock.tick(self.fps)
            # systems update #
            
        pygame.quit()
        