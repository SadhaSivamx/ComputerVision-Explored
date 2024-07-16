import cv2
import math as mt
import numpy as np
import matplotlib.pyplot as plt

# Load the image (replace with your image path)
image = cv2.imread("IMG.png", cv2.IMREAD_GRAYSCALE)

# Check if the image was successfully loaded
if image is None:
    raise Exception("Could not load the image!")

# Perform Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Find the coordinates (x, y) of edge points
y_coords, x_coords = np.where(edges > 0)

# Calculate distances between consecutive edge points
NewGraph = []
RedPoints = []
Pre = 0
Count = 0
X = []
P1 = [x_coords[0], y_coords[0]]

for i, j in zip(x_coords, y_coords):
    P2 = [i, j]
    Distance = mt.sqrt(((P1[0] - P2[0]) ** 2) + ((P1[1] - P2[1]) ** 2))
    NewGraph.append(Distance)
    if abs(Pre - Distance) >= 30:
        X.append(Count)
        RedPoints.append(Distance)
    Pre = Distance
    Count += 1
    P1 = P2

# Plotting
plt.figure(figsize=(15, 8))

# Original Image and Canny Edge Detection
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')

# Scatter plot of edge points
plt.subplot(2, 2, 3)
plt.scatter(x_coords, y_coords, s=1, c='b')
plt.title('Edge Points')
plt.axis('off')

# Distance plot with red points marked
plt.subplot(2, 2, 4)
plt.plot(range(1, len(NewGraph) + 1), NewGraph, marker='o', markersize=2, linestyle='-')
plt.scatter(X, RedPoints, c='r', label='Red Points')
plt.title('Distance Between Consecutive Edge Points')
plt.xlabel('Index')
plt.ylabel('Distance')
plt.legend()
plt.axis('off')

plt.tight_layout()
plt.show()
