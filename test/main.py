# main.py #
import sys, os
import pygame

# append src path so imports work and make it readable, not blind #
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# imports
from gameEngine import gEngine
from pylon2d.PlayerSystem.component import Position, Velocity, Sprite
from pylon2d.AIBehavior.aiSystem import AI
from pylon2d.entity import Entity
from pylon2d.SpeedZone.speedSys import SpeedZoneSys
from pylon2d.SpeedZone.speed_component import SpeedZone

def main():
    engine = gEngine(800, 600, 60)

    # player entity section #
    player_surf = pygame.Surface((50, 50))
    player_surf.fill((255, 0, 0))
    player = Entity()
    player.addComponent(Position(100, 100))
    player.addComponent(Velocity(3, 2))
    player.addComponent(Sprite(player_surf))
    engine.addEntity(player)

    # wanderer AI section #
    wanderer_surf = pygame.Surface((50, 50))
    wanderer_surf.fill((0, 0, 255))
    wanderer = Entity()
    wanderer.addComponent(Position(75, 75))
    wanderer.addComponent(Velocity(2, 2))
    wanderer.addComponent(Sprite(wanderer_surf))
    wanderer.addComponent(AI(speed=3))
    engine.addEntity(wanderer)

    # speed zones (testing) #
    engine.speed_zones = [
        SpeedZone(150, 150, 100, 50, boost=2),
        SpeedZone(300, 300, 150, 75, boost=1.5),
    ]
    engine.speed_sys = SpeedZoneSys()

    engine.runner()

if __name__ == "__main__":
    main()
