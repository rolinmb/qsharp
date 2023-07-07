import qsharp
from HostPython import RandomBit
import numpy as np
import os

def qsharp_random_bit():
    return RandomBit.simulate()

def numpy_random_bit():
    return np.random.binomial(1, 0.5)

def get_true_random():
    return int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)