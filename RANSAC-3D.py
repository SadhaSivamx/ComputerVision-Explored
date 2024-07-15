import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate_random_points_3d(num_points=5):
    points = []
    for _ in range(num_points):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(-10, 10)
        points.append([x, y, z])
    return points


# Generate a sample dataset with 10 points in 3D
random_points_3d = generate_random_points_3d(50)
print("Random Points (3D):", random_points_3d)

Final = 0
Points = 10000
BestPlane = None
Tolerance = 5


# Function to calculate plane parameters (A, B, C, D) from three points
def calculate_plane_parameters(p1, p2, p3):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    A = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
    B = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
    C = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    D = - (A * x1 + B * y1 + C * z1)
    return A, B, C, D


# Iterate over triplets of points to define planes
for i in range(len(random_points_3d)):
    for j in range(i + 1, len(random_points_3d)):
        for k in range(j + 1, len(random_points_3d)):
            P1 = random_points_3d[i]
            P2 = random_points_3d[j]
            P3 = random_points_3d[k]

            # Calculate plane parameters (A, B, C, D) for the plane passing through P1, P2, P3
            A, B, C, D = calculate_plane_parameters(P1, P2, P3)

            Tot = 0
            Now = 0

            # Count points within the tolerance distance from the plane and sum up distances
            for z in random_points_3d:
                if z == P1 or z == P2 or z == P3:
                    continue  # Skip the points used to define the plane

                # Calculate the perpendicular distance from point z to the plane Ax + By + Cz + D = 0
                x0, y0, z0 = z
                distance = abs(A * x0 + B * y0 + C * z0 + D) / math.sqrt(A ** 2 + B ** 2 + C ** 2)

                if distance < Tolerance:
                    Tot += 1
                    Now += distance

            # Update the best plane if this one has more points within tolerance and less total distance
            if Tot > Final and Points > Now:
                Final = Tot
                BestPlane = (A, B, C, D)
                Points = Now

if BestPlane:
    print(f"Best Plane Parameters: A = {BestPlane[0]}, B = {BestPlane[1]}, C = {BestPlane[2]}, D = {BestPlane[3]}")
    print(f"Number of points within tolerance: {Final}")
else:
    print("No valid plane found.")


# Function to plot the best fit plane with perpendicular distances
def plot_best_fit_plane(points, A, B, C, D, tolerance):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot random points
    xs, ys, zs = zip(*points)
    ax.scatter(xs, ys, zs, color='red', label='Random Points')

    # Plot best fit plane
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    X, Y = np.meshgrid(np.linspace(xlim[0], xlim[1], 10), np.linspace(ylim[0], ylim[1], 10))
    Z = (-A * X - B * Y - D) / C
    ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='blue', edgecolor='none',
                    label='Best Fit Plane')

    # Plot perpendicular lines for points within tolerance
    for z in points:
        x0, y0, z0 = z
        distance = abs(A * x0 + B * y0 + C * z0 + D) / math.sqrt(A ** 2 + B ** 2 + C ** 2)

        if distance < tolerance:
            # Vector normal to the plane (A, B, C)
            normal = np.array([A, B, C])

            # Point on the plane
            point_on_plane = np.array([x0, y0, z0])

            # Projection of the point onto the plane
            projected_point = point_on_plane - (A * x0 + B * y0 + C * z0 + D) / (A ** 2 + B ** 2 + C ** 2) * normal

            # Plot line segment from the point to the projection
            ax.plot([x0, projected_point[0]], [y0, projected_point[1]], [z0, projected_point[2]], 'k--', linewidth=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Best Fit Plane and Random Points with Perpendicular Distances')
    ax.legend()
    plt.show()


# Plot the best fit plane if a valid plane is found
if BestPlane:
    plot_best_fit_plane(random_points_3d, BestPlane[0], BestPlane[1], BestPlane[2], BestPlane[3], Tolerance)
