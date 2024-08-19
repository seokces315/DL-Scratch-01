import numpy as np
import matplotlib.pyplot as plt


# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Inputs
x = np.arange(-5.0, 5.0, 0.1)
# Processing
y = sigmoid(x)
# Plot the results
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
