import numpy as np


# AND Gate
def AND(x1, x2):

    # Inputs
    x = np.array([x1, x2])
    # Weights & Bias
    w = np.array([0.5, 0.5])
    b = -0.99

    # Linear combination
    lin_comb = np.sum(x * w) + b

    # Gate
    if lin_comb <= 0:
        return 0
    elif lin_comb > 0:
        return 1


# NAND Gate
def NAND(x1, x2):

    # Inputs
    x = np.array([x1, x2])
    # Weights & Bias
    w = np.array([-0.5, -0.5])
    b = 0.99

    # Linear combination
    lin_comb = np.sum(x * w) + b

    # Gate
    if lin_comb <= 0:
        return 0
    elif lin_comb > 0:
        return 1


# OR Gate
def OR(x1, x2):

    # Inputs
    x = np.array([x1, x2])
    # Weights & Bias
    w = np.array([0.5, 0.5])
    b = -0.01

    # Linear combination
    lin_comb = np.sum(x * w) + b

    # Gate
    if lin_comb <= 0:
        return 0
    elif lin_comb > 0:
        return 1


# XOR Gate
def XOR(x1, x2):

    # Implement with other gates
    o1 = NAND(x1, x2)
    o2 = OR(x1, x2)
    res = AND(o1, o2)

    return res


# Actual results
output1 = XOR(0, 0)
output2 = XOR(1, 0)
output3 = XOR(0, 1)
output4 = XOR(1, 1)

print(output1)
print(output2)
print(output3)
print(output4)
