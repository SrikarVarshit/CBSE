import os
import sys
# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Given point A
A = np.array([[2], [-8]])

# Nearest point P on the parabola y^2 = 4x
P = np.array([[4], [-4]])

# Distance calculation
min_dist = np.linalg.norm(P - A)
print(f"Given Point A: ({A[0, 0]}, {A[1, 0]})")
print(f"Nearest Point on Parabola P: ({P[0, 0]}, {P[1, 0]})")
print(f"Minimum Distance: {min_dist:.4f} units (sqrt(20))")

# Generate parabola: y^2 = 4x => x = y^2 / 4
y_vals = np.linspace(-10, 6, 400)
x_vals = (y_vals**2) / 4

# Normal line segment AP (shortest distance) using CoordGeo
line_AP = line_gen(A, P)

# Tangent line at P(4, -4): slope m_t = 2 / y = -0.5
# Equation: y + 4 = -0.5*(x - 4) => y = -0.5*x - 2
x_tan = np.linspace(0, 8, 50)
y_tan = -0.5 * x_tan - 2
tan_start = np.array([[x_tan[0]], [y_tan[0]]])
tan_end = np.array([[x_tan[-1]], [y_tan[-1]]])
line_tan = line_gen(tan_start, tan_end)

plt.figure(figsize=(8, 7))

# Plot parabola curve
plt.plot(x_vals, y_vals, label=r'Parabola: $y^2 = 4x$', color='navy', linewidth=2)

# Plot normal segment AP (shortest distance vector)
plt.plot(line_AP[0, :], line_AP[1, :], label=r'Normal Segment $AP$ (Shortest Dist)', color='crimson', linewidth=2.5, linestyle='--')

# Plot tangent line at P
plt.plot(line_tan[0, :], line_tan[1, :], label=r'Tangent at $P(4, -4)$', color='darkgreen', linewidth=1.5, linestyle=':')

# Scatter points A and P
pts = np.block([[A, P]])
plt.scatter(pts[0, :], pts[1, :], color='black', zorder=5)

# Annotations
plt.annotate(r'$A(2, -8)$', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(-25, -15), fontweight='bold')
plt.annotate(r'$P(4, -4)$ [Nearest Point]', (P[0, 0], P[1, 0]), textcoords="offset points", xytext=(12, 5), color='crimson', fontweight='bold')

# Configure axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('$x$', fontweight='bold')
plt.ylabel('$y$', fontweight='bold')
plt.title(rf'Question 31: Point on $y^2=4x$ Nearest to $(2,-8)$ (Dist = {min_dist:.2f})')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')
plt.axis('equal')

# Save and show
plot_file = 'q31_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
# subprocess.run(['termux-open', plot_file])
plt.show()
