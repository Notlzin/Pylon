from ..PlayerSystem.component import Position, Velocity

class MovementSys:
    def update(self, entities):
        for entity in entities:
            pos = entity.getComponent(Position)
            vel = entity.getComponent(Velocity)
            if pos and vel:
                pos.x += vel.dx
                pos.y += vel.dy

