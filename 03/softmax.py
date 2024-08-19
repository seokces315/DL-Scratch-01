import numpy as np
import warnings

warnings.filterwarnings(action="ignore")


# Define softmax activation function
def softmax_(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


# Improved version
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # Solution
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


# Inputs
a = np.array([1010, 1000, 990])
# Overflow Problem
result1 = softmax_(a)
result2 = softmax(a)

print(result1)
print(result2)
