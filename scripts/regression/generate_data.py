import random
import math

def generate_dataset(
        n_samples: int,
        a: float,
        b: float,
        x_range,
        y_range=None,
        noise_std: float = 0.0,
        seed=None
):
    if seed is not None:
        random.seed(seed)

    dataset = []

    norm = math.sqrt(a * a + 1.0)
    nx = -a / norm
    ny =  1.0 / norm

    for _ in range(n_samples):
        x0 = random.uniform(*x_range)
        y0 = a * x0 + b

        t = random.gauss(0.0, noise_std)

        x = x0 + nx * t
        y = y0 + ny * t

        if y_range is not None:
            y = max(y_range[0], min(y, y_range[1]))

        dataset.append((x, y))

    return dataset