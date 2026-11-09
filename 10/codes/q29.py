import os
import sys
import subprocess
import matplotlib

# Headless backend for Termux
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Center and radii
O = np.array([[0], [0]])
r = 2.0  # Inner radius
R = 5.0  # Outer radius

# Point P on the outer circle
P = np.array([[R], [0.0]])

# Theoretical tangent length: sqrt(R^2 - r^2)
tangent_len = np.sqrt(R**2 - r**2)

# Contact points on the inner circle (r*cos(theta), r*sin(theta))
# cos(theta) = r / R = 2 / 5
cos_theta = r / R
sin_theta = np.sqrt(1 - cos_theta**2)

A = np.array([[r * cos_theta], [r * sin_theta]])
B = np.array([[r * cos_theta], [-r * sin_theta]])

print(f"Inner Circle Radius: {r} cm")
print(f"Outer Circle Radius: {R} cm")
print(f"Point P on outer circle: ({P[0, 0]:.1f}, {P[1, 0]:.1f})")
print(f"Contact point A: ({A[0, 0]:.2f}, {A[1, 0]:.2f})")
print(f"Contact point B: ({B[0, 0]:.2f}, {B[1, 0]:.2f})")
print(f"Calculated tangent length PA: {tangent_len:.2f} cm (sqrt(21))")

# Parametric circles
theta = np.linspace(0, 2 * np.pi, 300)
c_inner_x = r * np.cos(theta)
c_inner_y = r * np.sin(theta)

c_outer_x = R * np.cos(theta)
c_outer_y = R * np.sin(theta)

# Line segments using CoordGeo
x_PA = line_gen(P, A)
x_PB = line_gen(P, B)
x_OA = line_gen(O, A)
x_OB = line_gen(O, B)
x_OP = line_gen(O, P)

plt.figure(figsize=(8, 8))

# Plot concentric circles
plt.plot(c_inner_x, c_inner_y, label=r'Inner Circle ($r = 2\,$cm)', color='teal', linewidth=2)
plt.plot(c_outer_x, c_outer_y, label=r'Outer Circle ($R = 5\,$cm)', color='darkblue', linewidth=2)

# Plot tangent lines
plt.plot(x_PA[0, :], x_PA[1, :], color='crimson', linewidth=2, label=f'Tangents $PA, PB$ ({tangent_len:.2f} cm)')
plt.plot(x_PB[0, :], x_PB[1, :], color='crimson', linewidth=2)

# Plot radii to points of contact and line OP
plt.plot(x_OA[0, :], x_OA[1, :], color='gray', linestyle='--', linewidth=1.2, label='Normal Radii')
plt.plot(x_OB[0, :], x_OB[1, :], color='gray', linestyle='--', linewidth=1.2)
plt.plot(x_OP[0, :], x_OP[1, :], color='purple', linestyle=':', linewidth=1.5, label='Segment $OP$')

# Scatter key points
pts = np.block([[O, P, A, B]])
plt.scatter(pts[0, :], pts[1, :], color='black', zorder=5)

# Annotations
plt.annotate(r'$O(0, 0)$', (O[0, 0], O[1, 0]), textcoords="offset points", xytext=(-20, -15), fontweight='bold')
plt.annotate(r'$P(5, 0)$', (P[0, 0], P[1, 0]), textcoords="offset points", xytext=(10, -5), fontweight='bold')
plt.annotate(r'$A$', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(-10, 10), fontweight='bold')
plt.annotate(r'$B$', (B[0, 0], B[1, 0]), textcoords="offset points", xytext=(-10, -18), fontweight='bold')

# Configure axes
plt.axhline(0, color='black', linewidth=0.6)
plt.axvline(0, color='black', linewidth=0.6)
plt.xlabel('$x$ (cm)')
plt.ylabel('$y$ (cm)')
plt.title(r'Question 29: Tangents to Inner Circle from Point $P$ on Outer Circle')
plt.axis('equal')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')

# Save and auto-open in Termux
plot_file = 'q29_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open', plot_file])
