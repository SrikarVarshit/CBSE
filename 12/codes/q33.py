import os
import sys
# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Triangle vertices as 2D column vectors
A = np.array([[0], [1]])
B = np.array([[4], [9]])
C = np.array([[4], [13]])

# Area calculation via integration / determinant
# Area = \int_0^4 (3x + 1 - (2x + 1)) dx = [x^2 / 2]_0^4 = 8
area_integral = 0.5 * (4**2)

print(f"Vertex A (Intersection of y=2x+1 and y=3x+1): {A.ravel()}")
print(f"Vertex B (Intersection of y=2x+1 and x=4): {B.ravel()}")
print(f"Vertex C (Intersection of y=3x+1 and x=4): {C.ravel()}")
print(f"Area of Triangular Region: {area_integral:.2f} sq. units")

# Generate line segments for triangle perimeter using CoordGeo
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Extended lines for full geometric context
x_vals = np.linspace(-1, 5, 100)
y_line1 = 2 * x_vals + 1
y_line2 = 3 * x_vals + 1

plt.figure(figsize=(8, 7))

# Plot boundary lines
plt.plot(x_vals, y_line1, label=r'$y = 2x + 1$', color='darkblue', linestyle='--', linewidth=1.2)
plt.plot(x_vals, y_line2, label=r'$y = 3x + 1$', color='darkred', linestyle='--', linewidth=1.2)
plt.axvline(4, color='darkgreen', linestyle='--', linewidth=1.2, label=r'$x = 4$')

# Plot triangle edges
plt.plot(x_AB[0, :], x_AB[1, :], color='navy', linewidth=2.5)
plt.plot(x_BC[0, :], x_BC[1, :], color='green', linewidth=2.5)
plt.plot(x_CA[0, :], x_CA[1, :], color='crimson', linewidth=2.5)

# Fill bounded triangular region
tri_x = [A[0, 0], B[0, 0], C[0, 0]]
tri_y = [A[1, 0], B[1, 0], C[1, 0]]
plt.fill(tri_x, tri_y, color='gold', alpha=0.4, label=f'Area = {area_integral:.0f} sq. units')

# Scatter and annotate vertices
pts = np.block([[A, B, C]])
plt.scatter(pts[0, :], pts[1, :], color='black', s=50, zorder=5)

plt.annotate(r'$A(0, 1)$', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(-25, 5), fontweight='bold')
plt.annotate(r'$B(4, 9)$', (B[0, 0], B[1, 0]), textcoords="offset points", xytext=(10, -10), fontweight='bold')
plt.annotate(r'$C(4, 13)$', (C[0, 0], C[1, 0]), textcoords="offset points", xytext=(10, 5), fontweight='bold')

# Configure axes and grid
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('$x$', fontweight='bold')
plt.ylabel('$y$', fontweight='bold')
plt.title(rf'Question 33: Area of Triangular Region Bounded by Lines ($A = {area_integral:.0f}$)')
plt.xlim(-1, 5.5)
plt.ylim(-2, 16)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')

# Save and show
plot_file = 'q33_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
# subprocess.run(['termux-open', plot_file])
plt.show()
