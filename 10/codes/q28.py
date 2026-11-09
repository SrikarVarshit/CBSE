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

# Upper class limits and cumulative frequencies
x_pts = np.array([30, 40, 50, 60, 70, 80, 90, 100], dtype=float)
cf_pts = np.array([0, 7, 12, 20, 30, 36, 42, 50], dtype=float)

# Coordinates of the median point (N/2 = 25 -> x = 65)
N_half = 25.0
median_x = 65.0

print(f"Total frequency (N): {cf_pts[-1]}")
print(f"N / 2: {N_half}")
print(f"Median determined from ogive: {median_x}")

# Generate smooth line segments between consecutive points using CoordGeo
curve_pts = []
for i in range(len(x_pts) - 1):
    P1 = np.array([[x_pts[i]], [cf_pts[i]]])
    P2 = np.array([[x_pts[i + 1]], [cf_pts[i + 1]]])
    seg = line_gen(P1, P2)
    curve_pts.append(seg)
ogive_curve = np.hstack(curve_pts)

# Projection lines for the median: (0, 25) -> (65, 25) -> (65, 0)
P_y_axis = np.array([[20], [N_half]])
P_median = np.array([[median_x], [N_half]])
P_x_axis = np.array([[median_x], [0]])

proj_h = line_gen(P_y_axis, P_median)
proj_v = line_gen(P_median, P_x_axis)

plt.figure(figsize=(9, 6))

# Plot the ogive curve
plt.plot(ogive_curve[0, :], ogive_curve[1, :], color='blue', linewidth=2.5, label="Less Than Ogive")
plt.scatter(x_pts, cf_pts, color='red', zorder=5)

# Plot median reference projections
plt.plot(proj_h[0, :], proj_h[1, :], color='darkgreen', linestyle='--', linewidth=1.8, label=r'Median Projection ($N/2 = 25$)')
plt.plot(proj_v[0, :], proj_v[1, :], color='darkgreen', linestyle='--', linewidth=1.8)
plt.scatter([median_x], [N_half], color='darkgreen', zorder=6)

# Annotate points along the ogive
for x_val, y_val in zip(x_pts, cf_pts):
    plt.annotate(f'({int(x_val)}, {int(y_val)})', (x_val, y_val), textcoords="offset points", xytext=(-12, 8), fontsize=8)

# Annotate median intersection
plt.annotate(
    f'Median = {median_x:.0f}\n(at $cf = 25$)',
    (median_x, N_half),
    textcoords="offset points",
    xytext=(15, -15),
    fontweight='bold',
    color='darkgreen',
    arrowprops=dict(arrowstyle='->', color='darkgreen')
)

# Configure plot axes and grid
plt.xlabel('Upper Class Limits (Marks)', fontweight='bold')
plt.ylabel('Cumulative Frequency ($cf$)', fontweight='bold')
plt.title('Question 28: Less Than Type Ogive and Median Evaluation')
plt.xlim(25, 105)
plt.ylim(0, 55)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')

# Save and auto-open in Termux
plot_file = 'q28_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open', plot_file])
