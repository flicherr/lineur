import random

def generate_dataset(
    n_samples: int,
    a: float,
    b: float,
    x_range,
    y_range,
    seed=None
):
    if seed is not None:
        random.seed(seed)

    dataset = []

    for _ in range(n_samples):
        x1 = random.uniform(*x_range)
        x2 = random.uniform(*y_range)

        value = a * x1 + x2 + b
        label = 1 if value >= 0 else -1

        dataset.append((x1, x2, label))

    return dataset

