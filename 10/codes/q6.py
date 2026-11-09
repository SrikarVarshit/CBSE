import subprocess
import matplotlib

# Use headless backend for Termux
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Quadratic coefficients: ax^2 + bx + c = 0
a = 2
b = -4
c = 3

# Discriminant calculation
D = b**2 - 4 * a * c
vertex_x = -b / (2 * a)
vertex_y = a * (vertex_x**2) + b * vertex_x + c

print(f"Equation: {a}x^2 + ({b})x + {c} = 0")
print(f"Discriminant (D): {D}")
print(f"Vertex: ({vertex_x:.2f}, {vertex_y:.2f})")
print("Nature of roots: No real roots (complex conjugate roots)")

# Domain for plotting
x = np.linspace(-1, 3, 400)
y = a * x**2 + b * x + c

plt.figure(figsize=(8, 6))

# Plot quadratic curve
plt.plot(x, y, label=r'$f(x) = 2x^2 - 4x + 3$', color='crimson', linewidth=2)

# Axes
plt.axhline(0, color='black', linewidth=1, linestyle='-', label='$x$-axis ($y = 0$)')
plt.axvline(0, color='black', linewidth=0.8)

# Vertex point
plt.scatter([vertex_x], [vertex_y], color='navy', zorder=5)
plt.annotate(
    f'Vertex / Minimum ({vertex_x:.0f}, {vertex_y:.0f})\n$f(x) \\geq 1 > 0$',
    (vertex_x, vertex_y),
    textcoords="offset points",
    xytext=(15, 10),
    fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='navy')
)

plt.fill_between(x, y, 0, where=(y > 0), color='salmon', alpha=0.15, label='No Real Intercepts ($D < 0$)')

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('Question 6: Nature of Roots for $2x^2 - 4x + 3 = 0$')
plt.xlim(-1, 3)
plt.ylim(-1, 8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

# Save and automatically open in Termux
plot_file = 'q6_plot.png'
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

#subprocess.run(['termux-open', plot_file])
