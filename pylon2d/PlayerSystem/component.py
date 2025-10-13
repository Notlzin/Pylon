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
        
class Health:
    def __init__(self, hp=100):
        self.hp = hp