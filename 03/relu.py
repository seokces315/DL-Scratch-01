import numpy as np
import matplotlib.pyplot as plt


# ReLU function
def relu(x):
    return np.maximum(x, 0)


# Inputs
x = np.arange(-5.0, 5.0, 0.1)
# Processing
y = relu(x)
# Plot the results
plt.plot(x, y)
plt.ylim(-1.1, 5.1)
plt.show()
