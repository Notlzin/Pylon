# seq2seq.py # # still experimental #
# GPT-5 creation LOL #
import os
import json
import torch
import torch.nn as nn
import torch.optim as optim

class Seq2Seq(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.GRU(2, 32, batch_first=True)
        self.decoder = nn.Linear(32, 2)

    def forward(self, x):
        _, h = self.encoder(x)
        out = self.decoder(h[-1])
        return out

# loading trajectory #
def loadTrajectories(json_file):
    """
    Loads trajectory data from JSON.
    Each trajectory becomes a tensor of shape [seq_len, 2] (x, y)
    """
    with open(json_file, "r") as f:
        data = json.load(f)

    trajectories = []
    for traj in data:
        seq = []

        # handle nested "steps" or flat entries
        step = traj.get("step", [traj])
        for step_dict in step:
            if "x" in step_dict and "y" in step_dict:
                seq.append([step_dict["x"], step_dict["y"]])
            else:
                print("skipping invalid step:", step_dict)   # ofcourse this is GPT-5mini working in the code [note: unicode removed vruh] #

        if seq:
            trajectories.append(seq)

    return trajectories

model = Seq2Seq()
optimizer = optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.MSELoss()

if __name__ == "__main__":
    json_file = os.path.join(os.path.dirname(__file__), "pylon2d_motion.json")
    trajectories_len = len(loadTrajectories(json_file))
    print(f"loaded {trajectories_len} trajectories.")
