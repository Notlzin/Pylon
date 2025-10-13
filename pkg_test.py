import pylon2d
import pygame

def test_pkg_import():
    assert pylon2d is not None
    assert pygame is not None
    assert hasattr(pylon2d, 'MovementSystem')
    assert hasattr(pylon2d, 'Physics')
    assert hasattr(pylon2d, 'Render')
    assert hasattr(pylon2d, 'InputSystem')
    assert hasattr(pylon2d, 'AIBehavior')
    assert hasattr(pylon2d, 'FPSS')
