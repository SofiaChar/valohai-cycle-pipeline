import random


def generate_random_params(num_configs=10):
    # Epochs between 10 and 100
    epochs = [random.randint(10, 100) for _ in range(num_configs)]

    # Learning rates between 0.0001 and 0.1
    lrs = [round(random.uniform(0.0001, 0.1), 5) for _ in range(num_configs)]

    return epochs, lrs
