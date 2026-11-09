import os
import sys
#import subprocess
import matplotlib

# Headless backend for Termux
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Import line_gen from local CoordGeo package
sys.path.insert(0, os.path.abspath('CoordGeo'))
from line.funcs import line_gen

# Given point A and direction vector b as 3D column vectors
A = np.array([[2], [-1], [4]])
b = np.array([[1], [1], [-2]])

print(f"Given point A: ({A[0, 0]}, {A[1, 0]}, {A[2, 0]})")
print(f"Direction vector b: [{b[0, 0]}, {b[1, 0]}, {b[2, 0]}]^T")
print("Cartesian equation: (x - 2)/1 = (y + 1)/1 = (z - 4)/(-2)")

# Generate line points extending in both directions from A
P1 = A - 2 * b
P2 = A + 2 * b
line_pts = line_gen(P1, P2)

# 3D Plotting
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D line
ax.plot(
    line_pts[0, :], line_pts[1, :], line_pts[2, :],
    label=r'Line: $\frac{x-2}{1}=\frac{y+1}{1}=\frac{z-4}{-2}$',
    color='royalblue',
    linewidth=2.5
)

# Highlight point A
ax.scatter([A[0, 0]], [A[1, 0]], [A[2, 0]], color='crimson', s=60, label=r'Point $A(2, -1, 4)$', zorder=5)

# Plot direction vector b anchored at A
ax.quiver(
    A[0, 0], A[1, 0], A[2, 0],
    b[0, 0], b[1, 0], b[2, 0],
    length=1.5,
    color='darkgreen',
    normalize=True,
    linewidth=2,
    label=r'Direction $\vec{b} = \hat{i} + \hat{j} - 2\hat{k}$'
)

# Configure 3D labels and title
ax.set_xlabel('$x$', fontweight='bold')
ax.set_ylabel('$y$', fontweight='bold')
ax.set_zlabel('$z$', fontweight='bold')
ax.set_title('Question 5: 3D Line in Cartesian & Vector Form')
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.5)

# Save and auto-open in Termux
plot_file = 'q5_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open', plot_file])
