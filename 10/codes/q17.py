import os
import sys
import subprocess
import matplotlib

# Headless backend for Termux
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Add CoordGeo to the module search path and import
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Endpoints of line segment XY as column vectors
X = np.array([[6], [-6]])
Y = np.array([[-4], [-1]])

# Ratio m:n = 2:3 -> lambda = m / (m + n) = 2/5
m, n = 2, 3
A = (n * X + m * Y) / (m + n)

# Solve for k from: 3x + k(y + 1) = 0 => k = -3x / (y + 1)
k = -3 * A[0, 0] / (A[1, 0] + 1)

print(f"Point X: {X.ravel()}")
print(f"Point Y: {Y.ravel()}")
print(f"Section point A: ({A[0, 0]:.1f}, {A[1, 0]:.1f})")
print(f"Calculated parameter k: {k:.1f}")

# Generate line segment XY using CoordGeo
x_XY = line_gen(X, Y)

# Generate intersecting line: 3x + 2y + 2 = 0 -> y = -(3x + 2)/2
P1 = np.array([[-2], [2]])
P2 = np.array([[4], [-7]])
x_line_k = line_gen(P1, P2)

plt.figure(figsize=(8, 6))

# Plot segment XY and line 3x + k(y + 1) = 0
plt.plot(x_XY[0, :], x_XY[1, :], label=r'Segment $XY$', color='navy', linewidth=2.5)
plt.plot(x_line_k[0, :], x_line_k[1, :], label=rf'Line: $3x + {int(k)}(y + 1) = 0$', color='crimson', linestyle='--', linewidth=2)

# Scatter points X, Y, and A
pts = np.block([[X, Y, A]])
plt.scatter(pts[0, :], pts[1, :], color='black', zorder=5)

# Annotate points
plt.annotate(r'$X(6, -6)$', (X[0, 0], X[1, 0]), textcoords="offset points", xytext=(10, -10), fontweight='bold')
plt.annotate(r'$Y(-4, -1)$', (Y[0, 0], Y[1, 0]), textcoords="offset points", xytext=(-25, 10), fontweight='bold')
plt.annotate(r'$A(2, -4)$', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(12, 5), color='crimson', fontweight='bold')

# Axes and grid styling
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(rf'Question 17: Section Point $A(2,-4)$ and Line Intersection ($k = {int(k)}$)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.axis('equal')

# Save and auto-open in Termux
plot_file = 'q17_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open', plot_file])
