# src/LAN/client.py #
import sys, os
import dotenv
import pygame
import socket
import pickle

# appending src for ECS accessing #
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# local importing #
from pylon2d.entity import Entity
from pylon2d.PlayerSystem.component import Position, Velocity, Sprite
from pylon2d.InputSystem.playerMovement import Controller

# server settings #
dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
dotenv.load_dotenv(dotenv_path=dotenv_path)
HOST = "127.0.0.1"
PORT = int(os.getenv("PORT", 5555))

# pygame setup #
W, H = 800, 600
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("client window [multiplayer]")
clock = pygame.time.Clock()
FPS = 60

# socket connect #
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# entities setup #
entities = []

# movement controller #
controller = Controller(speed=4)
running = True

# [optional]: color palette for other clients #
colors = [
    (0, 255, 0), (0, 0, 255), (255, 0, 0),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# receive initial state #
try:
    init_data = pickle.loads(client_socket.recv(4096))
    controlled_entityID = init_data["entity_id"]   # [GPT]FIXED: match server.py #

    for e_id, x, y in init_data["entities"]:
        while e_id >= len(entities):
            surface = pygame.Surface((50, 50))
            surface.fill(colors[e_id % len(colors)])
            e = Entity()
            e.addComponent(Position(x, y))
            e.addComponent(Velocity(0, 0))
            e.addComponent(Sprite(surface))
            entities.append(e)   # [GPT]FIXED: append entities properly #
except Exception as e:
    import traceback
    print("[INITIALIZATION_ERROR]", e)
    traceback.print_exc()
    pygame.quit()
    client_socket.close()
    sys.exit()

# main loop
while running:
    dt = clock.tick(FPS)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # local input
    if 0 <= controlled_entityID < len(entities):
        controlled_e = entities[controlled_entityID]
        controller.update([controlled_e])

        # send input -> server
        vel = controlled_e.getComponent(Velocity)
        inp_data = [(controlled_entityID, vel.dx, vel.dy) if vel else (controlled_entityID, 0, 0)]
        try:
            client_socket.sendall(pickle.dumps(inp_data))
        except Exception as e:
            print("[SEND_ERROR]:", e)

    # receive updates from server #
    try:
        data = client_socket.recv(4096)
        if data:
            positions = pickle.loads(data)["entities"]
            for entity_id, x, y in positions:
                # expand entities list if needed #
                while entity_id >= len(entities):
                    new_surf = pygame.Surface((50, 50))
                    new_surf.fill(colors[entity_id % len(colors)])
                    new_entity = Entity()
                    new_entity.addComponent(Position(0, 0))
                    new_entity.addComponent(Velocity(0, 0))
                    new_entity.addComponent(Sprite(new_surf))
                    entities.append(new_entity)

                pos = entities[entity_id].getComponent(Position)
                if pos:
                    pos.x = x
                    pos.y = y
    except Exception as e:
        import traceback
        print("[CLIENT_ERROR OR RECV_ERROR]:", e)
        traceback.print_exc()

    # rendering #
    screen.fill((0, 0, 0))
    for e_id, e in enumerate(entities):
        pos = e.getComponent(Position)
        spr = e.getComponent(Sprite)
        if pos and spr and spr.surface:
            screen.blit(spr.surface, (pos.x, pos.y))
    pygame.display.flip()

pygame.quit()
client_socket.close()
