# datagen.py #
# yeah this is GPT-5 creation LOL #
import numpy as np
import json

def generate_json_dataset(n_entities=10, steps=300, width=800, height=600, max_speed=5.0):
    data = []
    for eid in range(n_entities):
        x, y = np.random.rand() * width, np.random.rand() * height
        dx, dy = np.random.uniform(-max_speed, max_speed, size=2)

        entity_data = []
        for step in range(steps):
            # bounce at borders
            if x <= 0 or x >= width:
                dx *= -1
            if y <= 0 or y >= height:
                dy *= -1

            # add random small changes #
            dx += np.random.randn() * 0.1
            dy += np.random.randn() * 0.1

            # move #
            x += dx
            y += dy

            # keep inside bounds #
            x = np.clip(x, 0, width)
            y = np.clip(y, 0, height)

            entity_data.append({
                "step": step,
                "x": float(x),
                "y": float(y),
                "dx": float(dx),
                "dy": float(dy)
            })
        data.append({
            "entity_id": eid,
            "trajectory": entity_data
        })

    # save as JSON
    with open("pylon2d_motion.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(data)} entities with {steps} steps each to pylon2d_motion.json")
    return data

# generate it!
dataset = generate_json_dataset()
