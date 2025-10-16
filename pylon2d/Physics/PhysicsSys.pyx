# PhysicsSys.pyx aka the Cython edition #
from pylon2d.PlayerSystem.component import Position, Velocity, Sprite
from libc.math cimport fmax, fmin

cdef class Physics:
    cdef public double w, h
    cdef public double friction

    def __init__(self, double w, double h, double friction=0.85):
        self.w = w
        self.h = h
        self.friction = friction

    def update(self, entities):
        cdef int i, j
        cdef object ent1, ent2
        cdef object pos1, pos2, vel1, vel2, spr1, spr2
        cdef int w1, h1, w2, h2

        # apply movement and boundary collisions [note: GPT-5 comments because i have to rebuild this over and over and over again] #
        for ent1 in entities:
            pos1 = ent1.getComponent(Position)
            vel1 = ent1.getComponent(Velocity)
            spr1 = ent1.getComponent(Sprite)

            if pos1 is None or vel1 is None or spr1 is None:
                continue

            # apply velocity #
            pos1.x += vel1.dx
            pos1.y += vel1.dy

            # apply friction (woah new thing) #
            vel1.dx *= self.friction
            vel1.dy *= self.friction

            # tiny stoppings #
            if abs(vel1.dx) < 0.01:
                vel1.dx = 0
            if abs(vel1.dy) < 0.01:
                vel1.dy = 0

            # wall bounce (basic)
            w1, h1 = spr1.surface.get_size()
            if pos1.x < 0 or pos1.x + w1 > self.w:
                vel1.dx *= -1
            if pos1.y < 0 or pos1.y + h1 > self.h:
                vel1.dy *= -1

            # clamp inside window
            pos1.x = fmax(0.0, fmin(pos1.x, self.w - w1))
            pos1.y = fmax(0.0, fmin(pos1.y, self.h - h1))

        # collision handling (the AABB)
        for i in range(len(entities)):
            ent1 = entities[i]
            pos1 = ent1.getComponent(Position)
            vel1 = ent1.getComponent(Velocity)
            spr1 = ent1.getComponent(Sprite)
            if pos1 is None or vel1 is None or spr1 is None:
                continue

            w1, h1 = spr1.surface.get_size()

            for j in range(i + 1, len(entities)):
                e2 = entities[j]
                pos2 = e2.getComponent(Position)
                vel2 = e2.getComponent(Velocity)
                spr2 = e2.getComponent(Sprite)
                if pos2 is None or vel2 is None or spr2 is None:
                    continue

                w2, h2 = spr2.surface.get_size()

                # AABB overlap check #
                if (pos1.x < pos2.x + w2 and
                    pos1.x + w1 > pos2.x and
                    pos1.y < pos2.y + h2 and
                    pos1.y + h1 > pos2.y):

                    # simple response: swap velocities [bounce] #
                    vel1.dx, vel2.dx = -vel2.dx, -vel1.dx
                    vel1.dy, vel2.dy = -vel2.dy, -vel1.dy
