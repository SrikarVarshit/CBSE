import os
import sys
# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Coterminous edge vectors as 3D column vectors
a = np.array([[-3], [7], [5]])
b = np.array([[-5], [7], [-3]])
c = np.array([[7], [-5], [-3]])
O = np.array([[0], [0], [0]])

# Matrix of edges and scalar triple product
M = np.hstack((a, b, c))
det_M = np.linalg.det(M)
volume = np.abs(det_M)

print(f"Matrix of coterminous edges [a, b, c]:\n{M}")
print(f"Scalar Triple Product (det): {det_M:.2f}")
print(f"Volume of Parallelepiped: {volume:.2f} cubic units")

# Define the 8 vertices of the parallelepiped
v0 = O
v1 = a
v2 = b
v3 = c
v4 = a + b
v5 = a + c
v6 = b + c
v7 = a + b + c

# 12 edges connecting the vertices
edges = [
    (v0, v1), (v0, v2), (v0, v3),
    (v1, v4), (v1, v5),
    (v2, v4), (v2, v6),
    (v3, v5), (v3, v6),
    (v4, v7), (v5, v7), (v6, v7)
]

# 3D Plotting
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Draw the 12 wireframe edges using line_gen from CoordGeo
for p_start, p_end in edges:
    seg = line_gen(p_start, p_end)
    ax.plot(seg[0, :], seg[1, :], seg[2, :], color='gray', linestyle='--', linewidth=1)

# Highlight the 3 primary coterminous vectors
seg_a = line_gen(O, a)
seg_b = line_gen(O, b)
seg_c = line_gen(O, c)

ax.plot(seg_a[0, :], seg_a[1, :], seg_a[2, :], color='red', linewidth=2.5, label=r'$\vec{a} = -3\hat{i}+7\hat{j}+5\hat{k}$')
ax.plot(seg_b[0, :], seg_b[1, :], seg_b[2, :], color='blue', linewidth=2.5, label=r'$\vec{b} = -5\hat{i}+7\hat{j}-3\hat{k}$')
ax.plot(seg_c[0, :], seg_c[1, :], seg_c[2, :], color='green', linewidth=2.5, label=r'$\vec{c} = 7\hat{i}-5\hat{j}-3\hat{k}$')

# Scatter vertices
vertices = np.block([[v0, v1, v2, v3, v4, v5, v6, v7]])
ax.scatter(vertices[0, :], vertices[1, :], vertices[2, :], color='black', s=30, zorder=5)

# Annotations
ax.text(O[0, 0], O[1, 0], O[2, 0], '  O(0,0,0)', fontweight='bold')
ax.text(a[0, 0], a[1, 0], a[2, 0], '  A', color='red', fontweight='bold')
ax.text(b[0, 0], b[1, 0], b[2, 0], '  B', color='blue', fontweight='bold')
ax.text(c[0, 0], c[1, 0], c[2, 0], '  C', color='green', fontweight='bold')

# Configure axes and title
ax.set_xlabel('$x$', fontweight='bold')
ax.set_ylabel('$y$', fontweight='bold')
ax.set_zlabel('$z$', fontweight='bold')
ax.set_title(rf'Question 10: Parallelepiped Volume = {volume:.0f} cu units')
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.5)

# Save and display
plot_file = 'q10_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
# subprocess.run(['termux-open', plot_file])
plt.show()
