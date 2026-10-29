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

# Known points B and C as column vectors
B = np.array([[-4], [6]])
C = np.array([[-2], [3]])

# Representative point A satisfying 3x + 2y = 0 (e.g., x = 2 -> y = -3)
A = np.array([[2], [-3]])

# Check collinearity via determinant of displacement vectors: det([B - A, C - B])
v1 = B - A
v2 = C - B
M = np.hstack((v1, v2))
det_M = np.linalg.det(M)

print(f"Matrix [v1, v2]:\n{M}")
print(f"Determinant: {det_M:.4f} (Collinear condition satisfied: {np.isclose(det_M, 0.0)})")
print("Collinear relation: 3x + 2y = 0")

# Line endpoints for visualization extending beyond B and A
P1 = np.array([[-6], [9]])
P2 = np.array([[4], [-6]])
x_line = line_gen(P1, P2)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_line[0, :], x_line[1, :], label=r'Collinear Line: $3x + 2y = 0$', color='royalblue', linewidth=2)

# Scatter points
pts = np.block([[B, C, A]])
plt.scatter(pts[0, :], pts[1, :], color='crimson', zorder=5)

# Annotate points
plt.annotate(r'$B(-4, 6)$', (B[0, 0], B[1, 0]), textcoords="offset points", xytext=(-20, 10), fontweight='bold')
plt.annotate(r'$C(-2, 3)$', (C[0, 0], C[1, 0]), textcoords="offset points", xytext=(10, 10), fontweight='bold')
plt.annotate(r'$A(2, -3)$ [Example $A(x, y)$]', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(10, -15), fontweight='bold')

# Configure axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Question 14: Collinear Points $A(x,y)$, $B(-4,6)$, $C(-2,3)$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.axis('equal')

# Save and auto-open in Termux
plot_file = 'q14_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open', plot_file])
