import random
import math


def generate_random_points(num_points=5):
    points = []
    for _ in range(num_points):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        points.append([x, y])
    return points


# Generate a sample dataset with 5 points
random_points = generate_random_points(5)
print("Random Points:", random_points)

Final = 0
BestLine = None
Tolerance = 3

# Iterate over pairs of points
for i in range(len(random_points)):
    for j in range(i + 1, len(random_points)):
        P1 = random_points[i]
        P2 = random_points[j]

        # Calculate the slope (M) and y-intercept (C) of the line passing through P1 and P2
        if P2[0] != P1[0]:
            M = (P2[1] - P1[1]) / (P2[0] - P1[0])
            C = P2[1] - M * P2[0]
        else:
            continue  # Skip vertical lines to avoid division by zero

        Tot = 0

        # Count points within the tolerance distance from the line
        for z in random_points:
            if z == P1 or z == P2:
                continue  # Skip the points used to define the line

            # Calculate the perpendicular distance from point z to the line y = Mx + C
            x0, y0 = z
            distance = abs(M * x0 - y0 + C) / math.sqrt(M ** 2 + 1)

            if distance < Tolerance:
                Tot += 1

        # Update the best line if this one has more points within tolerance
        if Tot > Final:
            Final = Tot
            BestLine = (M, C)

if BestLine:
    print(f"Best Line: Slope (M) = {BestLine[0]}, Y-intercept (C) = {BestLine[1]}")
    print(f"Number of points within tolerance: {Final}")
else:
    print("No valid line found.")

# Optional: Plotting the best fit line
import matplotlib.pyplot as plt
import numpy as np


def plot_best_fit_line(points, m, c, tolerance):
    x_vals = np.linspace(-10, 10, 100)
    y_vals = m * x_vals + c

    plt.figure(figsize=(8, 6))
    plt.scatter(*zip(*points), color='red', label='Random Points')
    plt.plot(x_vals, y_vals, color='blue', label=f'Best Fit Line (M={m}, C={c})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Best Fit Line and Random Points')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


# Plot the best fit line if a valid line is found
if BestLine:
    plot_best_fit_line(random_points, BestLine[0], BestLine[1], Tolerance)
