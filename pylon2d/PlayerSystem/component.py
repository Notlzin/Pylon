# components for movement and position #
# components.py #

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy

class Sprite:
    def __init__(self, surface):
        self.surface = surface
        self.render_surface = None
        self.layer = 0

# this is unused, so if you can find an implementation, dont (if you wanna contribute to the repo directly) or implement it yourself (fork it) #
class Gravity:
    def __init__(self, force=0.6, terminalVel=9):
        self.force = force
        self.terminalVel = terminalVel

# another unused class... hmm #
class Health:
    def __init__(self, hp=100):
        self.max = hp
        self.current = hp

class HealthBar:
    def __init__(self, owner):
        self.owner = owner
