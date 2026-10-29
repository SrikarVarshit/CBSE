import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add CoordGeo directory to module search path
sys.path.insert(0, os.path.abspath('CoordGeo'))

try:
    from line.funcs import line_gen
except ImportError:
    # Standalone fallback if CoordGeo is not in the execution directory
    def line_gen(A, B):
        len_pts = 10
        dim = A.shape[0]
        x_AB = np.zeros((dim, len_pts))
        lam_1 = np.linspace(0, 1, len_pts)
        for i in range(len_pts):
            temp1 = A + lam_1[i] * (B - A)
            x_AB[:, i] = temp1.T
        return x_AB

# Define the points as 2D column vectors
A = np.array([[-2], [0]])
B = np.array([[6], [0]])
P = np.array([[2], [0]])

# Verify distance analytically
dist_PA = np.linalg.norm(P - A)
dist_PB = np.linalg.norm(P - B)
print(f"Coordinates of P: ({P[0,0]:.1f}, {P[1,0]:.1f})")
print(f"Distance PA = {dist_PA:.2f}")
print(f"Distance PB = {dist_PB:.2f}")

# Generate line segment AB
x_AB = line_gen(A, B)

# Perpendicular bisector line through P (x = 2)
y_vals = np.linspace(-3, 3, 100)
x_bisector = np.full_like(y_vals, P[0, 0])

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_AB[0, :], x_AB[1, :], label='Segment $AB$', color='blue', linewidth=2)
plt.plot(x_bisector, y_vals, label='Perpendicular Bisector ($x = 2$)', color='purple', linestyle='--')

# Scatter points
tri_coords = np.block([[A, B, P]])
plt.scatter(tri_coords[0, :], tri_coords[1, :], color='red', zorder=5)

# Annotate points
plt.annotate(f'A(-2, 0)', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(-25, 10))
plt.annotate(f'B(6, 0)', (B[0, 0], B[1, 0]), textcoords="offset points", xytext=(10, 10))
plt.annotate(f'P(2, 0)', (P[0, 0], P[1, 0]), textcoords="offset points", xytext=(-10, -18), fontweight='bold')

# Configure plot axes and grid
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Question 1: Point P Equidistant from A and B')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.axis('equal')

# Save and show
plt.savefig('q1_plot.png', dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open',plot_file])
