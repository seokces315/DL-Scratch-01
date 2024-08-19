import numpy as np
import matplotlib.pyplot as plt


# General step function
def step_function(x):
    flag = x > 0
    res = flag.astype(int)  # np.int32 or np.int64
    return res


# Inputs
x = np.arange(-5.0, 5.0, 0.1)
# Processing
y = step_function(x)
# Plot the results
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
