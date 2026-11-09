import os
import sys
# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Extreme corner points of the feasible region as column vectors
O = np.array([[0], [0]])
A = np.array([[3], [0]])
B = np.array([[2], [3]])
C = np.array([[0], [4]])

# Objective function coefficients: Z = 40x + 50y
c_obj = np.array([40, 50])

# Evaluate profit at each vertex
corners = [('O', O), ('A', A), ('B', B), ('C', C)]
print("Corner Point Evaluation for Z = 40x + 50y:")
max_val = -1
opt_point = None
for name, pt in corners:
    z_val = np.dot(c_obj, pt.flatten())
    print(f"Point {name}({pt[0, 0]}, {pt[1, 0]}): Z = Rs. {z_val:.0f}")
    if z_val > max_val:
        max_val = z_val
        opt_point = (name, pt)

print(f"\nMaximum Profit: Rs. {max_val:.0f} at Point {opt_point[0]}({opt_point[1][0, 0]}, {opt_point[1][1, 0]})")

# Generate boundary lines across quadrant using CoordGeo line_gen
# Line 1: 3x + y = 9 -> intercepts (0, 9) and (3, 0)
L1_start = np.array([[0], [9]])
L1_end = np.array([[3.2], [-0.6]])
x_L1 = line_gen(L1_start, L1_end)

# Line 2: x + 2y = 8 -> intercepts (0, 4) and (8, 0)
L2_start = np.array([[-0.5], [4.25]])
L2_end = np.array([[8.5], [-0.25]])
x_L2 = line_gen(L2_start, L2_end)

# Perimeter segments of the feasible polygon
seg_OA = line_gen(O, A)
seg_AB = line_gen(A, B)
seg_BC = line_gen(B, C)
seg_CO = line_gen(C, O)

plt.figure(figsize=(9, 7))

# Plot full constraint boundary lines
plt.plot(x_L1[0, :], x_L1[1, :], label=r'Silver: $3x + y = 9$', color='navy', linestyle='--', linewidth=1.5)
plt.plot(x_L2[0, :], x_L2[1, :], label=r'Gold: $x + 2y = 8$', color='purple', linestyle='--', linewidth=1.5)

# Plot polygon edges
plt.plot(seg_OA[0, :], seg_OA[1, :], color='black', linewidth=2)
plt.plot(seg_AB[0, :], seg_AB[1, :], color='black', linewidth=2)
plt.plot(seg_BC[0, :], seg_BC[1, :], color='black', linewidth=2)
plt.plot(seg_CO[0, :], seg_CO[1, :], color='black', linewidth=2)

# Fill feasible region OABC
poly_x = [O[0, 0], A[0, 0], B[0, 0], C[0, 0]]
poly_y = [O[1, 0], A[1, 0], B[1, 0], C[1, 0]]
plt.fill(poly_x, poly_y, color='limegreen', alpha=0.35, label='Feasible Region ($OABC$)')

# Scatter corner points
pts = np.block([[O, A, B, C]])
plt.scatter(pts[0, :], pts[1, :], color='black', s=50, zorder=5)

# Highlight optimal point B(2, 3)
plt.scatter([B[0, 0]], [B[1, 0]], color='crimson', s=100, zorder=6, label=r'Optimal Point $B(2, 3)$')

# Annotations
plt.annotate(r'$O(0, 0)$' + '\n$Z=0$', (O[0, 0], O[1, 0]), textcoords="offset points", xytext=(-25, -15), fontweight='bold')
plt.annotate(r'$A(3, 0)$' + '\n$Z=120$', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(5, 5), fontweight='bold')
plt.annotate(r'$B(2, 3)$' + '\n' + r'$\mathbf{Z_{max}=230}$', (B[0, 0], B[1, 0]), textcoords="offset points", xytext=(12, 10), color='crimson', fontweight='bold')
plt.annotate(r'$C(0, 4)$' + '\n$Z=200$', (C[0, 0], C[1, 0]), textcoords="offset points", xytext=(-35, 10), fontweight='bold')

# Configure axes and grid
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlabel('Units of Type A ($x$)', fontweight='bold')
plt.ylabel('Units of Type B ($y$)', fontweight='bold')
plt.title(r'Question 36: LPP Graphical Solution ($Z_{\max} = 230$ at $(2, 3)$)')
plt.xlim(-0.8, 9)
plt.ylim(-0.8, 10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

# Save and show
plot_file = 'q36_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
# subprocess.run(['termux-open', plot_file])
plt.show()
