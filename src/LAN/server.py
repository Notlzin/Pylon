import socket
import threading
import pickle # for serializing python objects #
import sys, os
import random
from dotenv import load_dotenv

# grabbing src to load src stuff #
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..")))

from src.entity import Entity
from src.PlayerSystem.component import Position, Velocity, Sprite

# loading PORT from env #
load_dotenv()

# server settings #
HOST = '127.0.0.1' # basically localhost #
PORT = int(os.getenv("PORT", 5555))

# storing connected clients #
client = {}

# game state [really simple: list of entity position] #
game_entities = []

# locking for thread-safe ops #
lock = threading.Lock()

# client handling #
def handleClient(conn, addr):
    print(f"[NEW_CONNECTION]: {addr} connected.")
    global game_entities

    # send initial state to the new client immediately #
    with lock:
        entity_id = client[conn]
        positions = [(i, e.getComponent(Position).x, e.getComponent(Position).y) for i, e in enumerate(game_entities)]
        init_packet = {
            "type": "init",
            "entity_id": entity_id, 
            "entities": positions
            }
        conn.sendall(pickle.dumps(init_packet))

    try:
        while True:
            # client input receive #
            data = conn.recv(4096)
            if not data:
                break
            inp_data = pickle.loads(data)
            
            # update server-sided entity positions #
            with lock:
                for entity_id, dx, dy in inp_data:
                    if entity_id < len(game_entities):
                        pos = game_entities[entity_id].getComponent(Position)
                        if pos:
                            pos.x += dx
                            pos.y += dy

            # broadcast updated positions back to all the clients #
            with lock:
                positions = [(i, e.getComponent(Position).x, e.getComponent(Position).y) for i, e in enumerate(game_entities)]
                update_packets = {
                    "type": "update",
                    "entities": positions
                    }
                for c in list(client.keys()):
                    try:
                        c.sendall(pickle.dumps(update_packets))
                    except:
                        pass
                    
    except Exception as e:
        print(f"[ERROR]: {addr}: {e}")
    finally:
        with lock:
            entity_id = client[conn]
            # removing the entity from game_entities #
            game_entities[entity_id] = None # marked as gone (aka removed) #
            del client[conn]
        conn.close()
        print(f"[DISCONNECTED]: {addr} disconnected the game.")
        
# starting server #
def startServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER_LISTENING]: server listened on {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        with lock:
            # create unique entity #
            new_entity = Entity()
            new_entity.addComponent(Position(random.randint(50,200), random.randint(50,150)))
            new_entity.addComponent(Velocity(0,0))
            new_entity.addComponent(Sprite(None))
            game_entities.append(new_entity)
            entity_id = len(game_entities) - 1
            client[conn] = entity_id
        
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE_CONNECTIONS]: {threading.active_count() - 1}")
        
if __name__ == "__main__":
    # initialization #
    print("[SERVER_STARTING]: initializing server...")
    startServer()
                        
# end of code #