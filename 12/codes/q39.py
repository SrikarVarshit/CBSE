import os
import sys
# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Line definition: points P and Q as 3D column vectors
P = np.array([[2], [-1], [2]])
Q = np.array([[5], [3], [4]])
dir_line = Q - P

# Plane definition: points A, B, and C as 3D column vectors
A = np.array([[2], [0], [3]])
B = np.array([[1], [1], [5]])
C = np.array([[3], [2], [4]])

# Normal vector via cross product
AB = B - A
AC = C - A
n_raw = np.cross(AB.flatten(), AC.flatten())
n = (n_raw / -3).reshape(3, 1)  # Simplified: [1, -1, 1]^T
d_plane = np.dot(n.flatten(), A.flatten())

# Solve for intersection parameter lambda:
# n . (P + lambda * dir_line) = d_plane => lambda = (d_plane - n . P) / (n . dir_line)
lam = (d_plane - np.dot(n.flatten(), P.flatten())) / np.dot(n.flatten(), dir_line.flatten())
intersection_pt = P + lam * dir_line

print(f"Line passing through: P({P.ravel()}) and Q({Q.ravel()})")
print(f"Line Cartesian Equation: (x - 2)/3 = (y + 1)/4 = (z - 2)/2")
print(f"Plane Normal Vector: n = {n.ravel()}")
print(f"Plane Cartesian Equation: {int(n[0,0])}x - {int(abs(n[1,0]))}y + {int(n[2,0])}z = {int(d_plane)}")
print(f"Intersection Parameter lambda: {lam:.1f}")
print(f"Point of Intersection: ({intersection_pt[0,0]:.1f}, {intersection_pt[1,0]:.1f}, {intersection_pt[2,0]:.1f})")

# Generate line points extending across the plane using CoordGeo
line_start = P - 1.0 * dir_line
line_end = P + 1.5 * dir_line
line_pts = line_gen(line_start, line_end)

# Triangle ABC boundary on the plane
tri_AB = line_gen(A, B)
tri_BC = line_gen(B, C)
tri_CA = line_gen(C, A)

# Plane surface grid: z = d_plane - x + y
x_grid = np.linspace(-1, 6, 20)
y_grid = np.linspace(-3, 5, 20)
X, Y = np.meshgrid(x_grid, y_grid)
Z = d_plane - n[0, 0] * X - n[1, 0] * Y

# 3D Plotting
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot plane surface
ax.plot_surface(X, Y, Z, alpha=0.3, color='deepskyblue', edgecolor='none')

# Plot triangle ABC on the plane
ax.plot(tri_AB[0, :], tri_AB[1, :], tri_AB[2, :], color='blue', linewidth=1.5, label=r'$\Delta ABC$ on Plane')
ax.plot(tri_BC[0, :], tri_BC[1, :], tri_BC[2, :], color='blue', linewidth=1.5)
ax.plot(tri_CA[0, :], tri_CA[1, :], tri_CA[2, :], color='blue', linewidth=1.5)

# Plot the 3D intersecting line
ax.plot(
    line_pts[0, :], line_pts[1, :], line_pts[2, :],
    color='purple', linewidth=2.5,
    label=r'Line: $\vec{r} = P + \lambda \vec{d}$'
)

# Highlight points
pts_plane = np.block([[A, B, C]])
ax.scatter(pts_plane[0, :], pts_plane[1, :], pts_plane[2, :], color='navy', s=35)
ax.scatter([Q[0, 0]], [Q[1, 0]], [Q[2, 0]], color='purple', s=40, label=r'Point $Q(5, 3, 4)$')

# Highlight intersection point P
ax.scatter(
    [intersection_pt[0, 0]], [intersection_pt[1, 0]], [intersection_pt[2, 0]],
    color='crimson', s=80, zorder=6,
    label=r'Intersection $P(2, -1, 2)$'
)

# Annotations
ax.text(A[0, 0], A[1, 0], A[2, 0], '  A(2,0,3)', fontweight='bold')
ax.text(B[0, 0], B[1, 0], B[2, 0], '  B(1,1,5)', fontweight='bold')
ax.text(C[0, 0], C[1, 0], C[2, 0], '  C(3,2,4)', fontweight='bold')
ax.text(intersection_pt[0, 0], intersection_pt[1, 0], intersection_pt[2, 0], '  P(2, -1, 2)', color='crimson', fontweight='bold')

# Configure axes and title
ax.set_xlabel('$x$', fontweight='bold')
ax.set_ylabel('$y$', fontweight='bold')
ax.set_zlabel('$z$', fontweight='bold')
ax.set_title(r'Question 39: Intersection of Line and Plane at $(2, -1, 2)$')
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.5)

# Save and show
plot_file = 'q39_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
# subprocess.run(['termux-open', plot_file])
plt.show()
