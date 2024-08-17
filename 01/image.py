import matplotlib.pyplot as plt
from matplotlib.image import imread

# Load image
img = imread("../dataset/cactus.jpg")

# Displaying image
plt.imshow(img)
plt.show()
