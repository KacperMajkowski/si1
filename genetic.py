import time
import numpy as np


def mutate(array):
    noise = np.random.randint(0, 100, len(array))
    for i in range(len(array)):
        array[i] = (array[i] + noise[i]) % 4
    array.append(0)
