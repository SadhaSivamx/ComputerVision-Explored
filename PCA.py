import matplotlib.pyplot as plt
import numpy as np

# Generate random points
xpoints = [np.random.randint(1, 5) for _ in range(15)]
ypoints = [np.random.randint(1, 5) for _ in range(15)]

# Calculate the means of xpoints and ypoints
mx = np.mean(xpoints)
my = np.mean(ypoints)
print(f"Mean of X: {mx}, Mean of Y: {my}")

# Calculate the covariance
cov_xx = sum([(x - mx) ** 2 for x in xpoints]) / (len(xpoints) - 1)
cov_yy = sum([(y - my) ** 2 for y in ypoints]) / (len(ypoints) - 1)
cov_xy = sum([(x - mx) * (y - my) for x, y in zip(xpoints, ypoints)]) / (len(xpoints) - 1)

# Construct the covariance matrix
CovarianceMatrix = np.array([[cov_xx, cov_xy],
                             [cov_xy, cov_yy]])

print("Covariance Matrix:\n", CovarianceMatrix)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(CovarianceMatrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Plot the eigenvectors
plt.scatter(xpoints, ypoints)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Eigenvectors')
plt.grid(True)

# Plot eigenvectors starting from the mean
for i in range(len(eigenvalues)):
    vec = eigenvectors[:, i] * np.sqrt(eigenvalues[i])
    plt.arrow(mx, my, vec[0], vec[1],
              head_width=0.2, head_length=0.2,
              linewidth=2, color='green', label='Eigenvectors' if i == 0 else "")
plt.legend()
plt.show()
