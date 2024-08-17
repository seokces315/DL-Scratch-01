import numpy as np
import matplotlib.pyplot as plt

# Preparing Data
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# Plotting
plt.plot(x, y)
plt.show()
