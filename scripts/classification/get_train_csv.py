import json
import csv
from generate_data import generate_dataset

def load_config(path: str):
    with open(path, "r") as f:
        return json.load(f)

cfg = load_config("config.json")
data = generate_dataset(
        n_samples=cfg["n_samples"],
        a=cfg["line"]["a"],
        b=cfg["line"]["b"],
        x_range=cfg["x_range"],
        y_range=cfg["y_range"],
        seed=cfg.get("seed")
)

with open("train.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x1", "x2", "y"])
    writer.writerows(data)

