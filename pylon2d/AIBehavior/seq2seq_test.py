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

# --- Load JSON and flatten steps ---
def load_json_flat(json_file):
    """
    Loads flat step data from JSON.
    Returns tensors X (inputs: x,y) and Y (targets: dx,dy)
    """
    with open(json_file, "r") as f:
        raw_data = json.load(f)

    X_list, Y_list = [], []

    for step in raw_data:
        # handle single-step entries
        if "x" in step and "y" in step:
            X_list.append([step["x"], step["y"]])
            if "dx" in step and "dy" in step:
                Y_list.append([step["dx"], step["dy"]])
            else:
                Y_list.append([0.0, 0.0])  # fallback velocity
        else:
            print("skipping invalid step:", step)

    if not X_list:
        raise ValueError("No valid steps found in JSON")

    # convert to tensors
    X_tensor = torch.tensor(X_list, dtype=torch.float32).unsqueeze(0)  # [1, seq_len, 2]
    Y_tensor = torch.tensor(Y_list, dtype=torch.float32).unsqueeze(0)  # [1, seq_len, 2]
    return X_tensor, Y_tensor

# --- Mini-batch generator ---
def batch_generator(X, Y, batch_size=32):
    seq_len = X.size(1)
    for i in range(0, seq_len, batch_size):
        x_batch = X[:, i:i+batch_size, :]
        y_batch = Y[:, i:i+batch_size, :]
        yield x_batch, y_batch

# --- Model setup ---
model = Seq2Seq()
optimizer = optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.MSELoss()

if __name__ == "__main__":
    json_file = os.path.join(os.path.dirname(__file__), "pylon2d_motion.json")
    X_tensor, Y_tensor = load_json_flat(json_file)
    print(f"Loaded {X_tensor.size(1)} steps.")

    # --- Training loop (mini-batch) ---
    epochs = 3
    batch_size = 64

    for epoch in range(epochs):
        for x_batch, y_batch in batch_generator(X_tensor, Y_tensor, batch_size):
            optimizer.zero_grad()
            output = model(x_batch)
            # only compare last step of batch
            loss = criterion(output, y_batch[:, -1, :])
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.6f}")

    # --- Save model ---
    torch.save(model.state_dict(), os.path.join(os.path.dirname(__file__), "seq2seq_model.pt"))
    print("Model saved as seq2seq_model.pt")

