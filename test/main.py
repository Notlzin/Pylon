# main.py #
import sys, os
import pygame

# appending system (src) to make it readable #
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gameEngine import gEngine
from src.PlayerSystem.component import Position, Velocity, Sprite
from src.AIBehavior.aiSystem import AI
from src.entity import Entity  # assuming you made an Entity class [which i did] #

def main():
    engine = gEngine(800, 600, 60)

    # create test entity #
    surf = pygame.Surface((50, 50))
    surf.fill((255, 0, 0))  # red square #

    # entities section #
    player = Entity()
    player.addComponent(Position(100, 100))
    player.addComponent(Velocity(3, 2))   
    player.addComponent(Sprite(surf))     
    #------------------------------------#
    wanderer = Entity()
    wanderer.addComponent(Position(75, 75))
    wanderer.addComponent(Velocity(2,2))
    wanderer.addComponent(Sprite(surf))
    wanderer.addComponent(AI(speed=3))

    engine.addEntity(player)
    engine.addEntity(wanderer)
    engine.runner()

if __name__ == "__main__":
    main()