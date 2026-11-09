import os
import sys
# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Given points on Plane 1 as 3D column vectors
A = np.array([[1], [1], [-2]])
B = np.array([[2], [-1], [1]])
C = np.array([[1], [2], [1]])

# Given point on Plane 2
P2 = np.array([[2], [3], [7]])

# Normal vector n = AB x AC = [9, 3, -1]^T
AB = B - A
AC = C - A
n = np.cross(AB.flatten(), AC.flatten()).reshape(3, 1)
# Scale to positive leading coefficient: -(-9, -3, 1) -> (9, 3, -1)
n = -n

d1 = np.dot(n.flatten(), A.flatten())
d2 = np.dot(n.flatten(), P2.flatten())
norm_n = np.linalg.norm(n)
dist = np.abs(d2 - d1) / norm_n

print(f"Normal vector n: {n.ravel()}")
print(f"Plane 1: {n[0,0]}x + {n[1,0]}y + {n[2,0]}z = {d1}")
print(f"Plane 2 (through (2,3,7)): {n[0,0]}x + {n[1,0]}y + {n[2,0]}z = {d2}")
print(f"Perpendicular distance: {dist:.4f} units (6 / sqrt(91))")

# Nearest projection point of P2 onto Plane 1
# P1 = P2 - ((n . P2 - d1) / ||n||^2) * n
P1 = P2 - ((d2 - d1) / (norm_n**2)) * n

# Perpendicular distance segment between planes using CoordGeo
seg_dist = line_gen(P1, P2)

# Triangle ABC on Plane 1
tri_AB = line_gen(A, B)
tri_BC = line_gen(B, C)
tri_CA = line_gen(C, A)

# Grid for parallel plane surfaces: z = 9x + 3y - d
x_vals = np.linspace(0.5, 3, 15)
y_vals = np.linspace(0.5, 3.5, 15)
X, Y = np.meshgrid(x_vals, y_vals)
Z1 = (n[0, 0] * X + n[1, 0] * Y - d1) / (-n[2, 0])
Z2 = (n[0, 0] * X + n[1, 0] * Y - d2) / (-n[2, 0])

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot parallel plane surfaces
ax.plot_surface(X, Y, Z1, alpha=0.35, color='cyan')
ax.plot_surface(X, Y, Z2, alpha=0.35, color='orange')

# Plot triangle ABC on Plane 1
ax.plot(tri_AB[0, :], tri_AB[1, :], tri_AB[2, :], color='blue', linewidth=1.8, label=r'$\Delta ABC$ on $\Pi_1$')
ax.plot(tri_BC[0, :], tri_BC[1, :], tri_BC[2, :], color='blue', linewidth=1.8)
ax.plot(tri_CA[0, :], tri_CA[1, :], tri_CA[2, :], color='blue', linewidth=1.8)

# Plot perpendicular distance line connecting the planes
ax.plot(
    seg_dist[0, :], seg_dist[1, :], seg_dist[2, :],
    color='crimson', linewidth=3, linestyle='--',
    label=rf'Distance $D = {dist:.2f}$'
)

# Scatter points
pts_p1 = np.block([[A, B, C]])
ax.scatter(pts_p1[0, :], pts_p1[1, :], pts_p1[2, :], color='blue', s=35)
ax.scatter([P2[0, 0]], [P2[1, 0]], [P2[2, 0]], color='red', s=50, label=r'$P(2, 3, 7)$ on $\Pi_2$')
ax.scatter([P1[0, 0]], [P1[1, 0]], [P1[2, 0]], color='crimson', s=40)

# Annotations
ax.text(P2[0, 0], P2[1, 0], P2[2, 0], '  P(2, 3, 7)', color='red', fontweight='bold')
ax.text(A[0, 0], A[1, 0], A[2, 0], '  A', color='blue', fontweight='bold')

# Configure axes and title
ax.set_xlabel('$x$', fontweight='bold')
ax.set_ylabel('$y$', fontweight='bold')
ax.set_zlabel('$z$', fontweight='bold')
ax.set_title(r'Question 38: Parallel Planes $\Pi_1: 9x+3y-z=14$ and $\Pi_2: 9x+3y-z=20$')
ax.legend(loc='upper left')
ax.grid(True, linestyle=':', alpha=0.5)

# Save and show
plot_file = 'q38_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
# subprocess.run(['termux-open', plot_file])
plt.show()
