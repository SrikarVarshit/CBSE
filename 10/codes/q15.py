import sys
import os
import subprocess
import matplotlib

# Headless backend for Termux
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Add CoordGeo package to path
sys.path.insert(0, os.path.abspath('CoordGeo'))

try:
    from line.funcs import line_gen
except ImportError:
    def line_gen(A, B):
        len_pts = 10
        dim = A.shape[0]
        x_AB = np.zeros((dim, len_pts))
        lam_1 = np.linspace(0, 1, len_pts)
        for i in range(len_pts):
            temp1 = A + lam_1[i] * (B - A)
            x_AB[:, i] = temp1.T
        return x_AB

# Define triangle vertices as column vectors
A = np.array([[1], [-1]])
B = np.array([[-4], [6]])
C = np.array([[-3], [-5]])

# Displacement edge vectors with A as reference origin
u = B - A
v = C - A

# Area via matrix determinant
mat_uv = np.hstack((u, v))
area = 0.5 * np.abs(np.linalg.det(mat_uv))

print(f"Vertex A: {A.ravel()}")
print(f"Vertex B: {B.ravel()}")
print(f"Vertex C: {C.ravel()}")
print(f"Displacement matrix [u, v]:\n{mat_uv}")
print(f"Calculated Area: {area:.2f} sq. units")

# Generate line segments for all three edges
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plotting
plt.figure(figsize=(8, 7))

# Plot triangle perimeter
plt.plot(x_AB[0, :], x_AB[1, :], color='navy', linewidth=2, label=r'Edges $AB, BC, CA$')
plt.plot(x_BC[0, :], x_BC[1, :], color='navy', linewidth=2)
plt.plot(x_CA[0, :], x_CA[1, :], color='navy', linewidth=2)

# Fill enclosed triangle area
tri_x = [A[0, 0], B[0, 0], C[0, 0]]
tri_y = [A[1, 0], B[1, 0], C[1, 0]]
plt.fill(tri_x, tri_y, color='skyblue', alpha=0.35, label=f'Area = {area:.1f} sq. units')

# Scatter vertices
pts = np.block([[A, B, C]])
plt.scatter(pts[0, :], pts[1, :], color='crimson', zorder=5)

# Annotations
plt.annotate(r'$A(1, -1)$', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(10, -10), fontweight='bold')
plt.annotate(r'$B(-4, 6)$', (B[0, 0], B[1, 0]), textcoords="offset points", xytext=(-20, 10), fontweight='bold')
plt.annotate(r'$C(-3, -5)$', (C[0, 0], C[1, 0]), textcoords="offset points", xytext=(-25, -15), fontweight='bold')

# Configure axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(r'Question 15: Area of Triangle $\Delta ABC$ via Determinant')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.axis('equal')

# Save and auto-open in Termux
plot_file = 'q15_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open', plot_file])
