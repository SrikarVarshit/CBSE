import os
import sys
# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Given points as 3D column vectors
A = np.array([[2], [5], [-3]])
B = np.array([[-2], [-3], [5]])
C = np.array([[5], [3], [-3]])

# Displacement vectors in the plane
v1 = B - A
v2 = C - A

# Compute normal vector via cross product
n_raw = np.cross(v1.flatten(), v2.flatten())
n = (n_raw / 8).reshape(3, 1)  # Simplified: [2, 3, 4]^T
d = np.dot(n.flatten(), A.flatten())

print(f"Point A: {A.ravel()}")
print(f"Point B: {B.ravel()}")
print(f"Point C: {C.ravel()}")
print(f"Normal vector n: {n.ravel()}")
print(f"Cartesian equation: {int(n[0,0])}x + {int(n[1,0])}y + {int(n[2,0])}z = {int(d)}")
print(f"Vector equation: r . ({int(n[0,0])}i + {int(n[1,0])}j + {int(n[2,0])}k) = {int(d)}")

# Generate triangle boundary edges using CoordGeo line_gen
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plane surface grid: z = (d - n1*x - n2*y) / n3
x_grid = np.linspace(-4, 7, 20)
y_grid = np.linspace(-4, 7, 20)
X, Y = np.meshgrid(x_grid, y_grid)
Z = (d - n[0, 0] * X - n[1, 0] * Y) / n[2, 0]

# 3D Plotting
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot plane surface
ax.plot_surface(X, Y, Z, alpha=0.3, color='cyan', edgecolor='none')

# Plot triangle edges
ax.plot(x_AB[0, :], x_AB[1, :], x_AB[2, :], color='blue', linewidth=2, label=r'Triangle $\Delta ABC$')
ax.plot(x_BC[0, :], x_BC[1, :], x_BC[2, :], color='blue', linewidth=2)
ax.plot(x_CA[0, :], x_CA[1, :], x_CA[2, :], color='blue', linewidth=2)

# Scatter points
pts = np.block([[A, B, C]])
ax.scatter(pts[0, :], pts[1, :], pts[2, :], color='red', s=45, zorder=5)

# Annotations
ax.text(A[0, 0], A[1, 0], A[2, 0], '  A(2, 5, -3)', fontweight='bold')
ax.text(B[0, 0], B[1, 0], B[2, 0], '  B(-2, -3, 5)', fontweight='bold')
ax.text(C[0, 0], C[1, 0], C[2, 0], '  C(5, 3, -3)', fontweight='bold')

# Plot normal vector from triangle centroid
centroid = (A + B + C) / 3
ax.quiver(
    centroid[0, 0], centroid[1, 0], centroid[2, 0],
    n[0, 0], n[1, 0], n[2, 0],
    length=2.5,
    color='darkgreen',
    normalize=True,
    linewidth=2,
    label=r'Normal $\vec{n} = 2\hat{i}+3\hat{j}+4\hat{k}$'
)

# Configure axes and title
ax.set_xlabel('$x$', fontweight='bold')
ax.set_ylabel('$y$', fontweight='bold')
ax.set_zlabel('$z$', fontweight='bold')
ax.set_title(r'Question 30: Plane $2x + 3y + 4z = 7$ through $A, B, C$')
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.5)

# Save and show
plot_file = 'q30_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
# subprocess.run(['termux-open', plot_file])
plt.show()
