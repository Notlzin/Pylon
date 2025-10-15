# PhysicsSys.pyx aka the Cython edition #
from pylon2d.PlayerSystem.component import Position, Velocity, Sprite
from libc.math cimport fmax, fmin

cdef class Physics:
    cdef public double w, h

    def __init__(self, double w, double h):
        self.w = w # width #
        self.h = h # height #

    def update(self, entities):
        for entity in entities:
            pos = entity.getComponent(Position)
            vel = entity.getComponent(Velocity)
            spr = entity.getComponent(Sprite)
            if pos is not None and vel is not None and spr is not None:
                # basic boundary collision system #
                if pos.x < 0 or pos.x + spr.surface.get_width() > self.w and not None:
                    vel.dx *= -1 # horizontal bounce #
                if pos.y < 0 or pos.y + spr.surface.get_width() > self.h and not None:
                    vel.dy *= -1 # vertical bounce #
                # applying velocity #
                pos.x += vel.dx
                pos.y += vel.dy
                # clamping to the screen limit #
                w, h = spr.surface.get_size()
                pos.x = fmax(<double>0.0, fmin(pos.x, self.w - w))
                pos.y = fmax(<double>0.0, fmin(pos.y, self.h - h))
