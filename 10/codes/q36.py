import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Add CoordGeo package to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../CoordGeo')))

# Import geometry generators from CoordGeo with local fallback
try:
    from line.funcs import line_gen
    from conics.funcs import circ_gen
except ImportError:
    def line_gen(A, B):
        len_pts = 10
        dim = A.shape[0]
        x_AB = np.zeros((dim, len_pts))
        lam = np.linspace(0, 1, len_pts)
        for i in range(len_pts):
            x_AB[:, i] = A + lam[i] * (B - A)
        return x_AB

    def circ_gen(O, r):
        len_pts = 100
        theta = np.linspace(0, 2 * np.pi, len_pts)
        x_circ = np.zeros((2, len_pts))
        x_circ[0, :] = r * np.cos(theta)
        x_circ[1, :] = r * np.sin(theta)
        return (x_circ.T + O).T

# Circle parameters
r = 2.0  # Radius of inner circle
R = 5.0  # Radius of outer circle
O = np.array([0.0, 0.0])  # Common centre vector

# Point P on the outer circle
P = np.array([R, 0.0])

# Tangent contact points A and B on the inner circle
# Since OA is perpendicular to PA: cos(theta) = r / R
cos_theta = r / R
sin_theta = np.sqrt(1.0 - cos_theta**2)

A = np.array([r * cos_theta, r * sin_theta])
B = np.array([r * cos_theta, -r * sin_theta])

# Midpoint of OP for the geometric construction circle
M = (O + P) / 2.0
r_m = R / 2.0

# Calculate tangent length using norm
PA_len = np.linalg.norm(P - A)
print(f"Calculated tangent length PA: {PA_len:.2f} cm (Theoretical: {np.sqrt(21):.2f} cm)")

# Generate coordinate arrays for plotting
circ_inner = circ_gen(O, r)
circ_outer = circ_gen(O, R)
circ_aux = circ_gen(M, r_m)

x_PA = line_gen(P, A)
x_PB = line_gen(P, B)
x_OA = line_gen(O, A)
x_OB = line_gen(O, B)
x_OP = line_gen(O, P)

# Plotting
plt.figure(figsize=(7, 7))
plt.plot(circ_inner[0, :], circ_inner[1, :], label='Inner circle ($r = 2$)')
plt.plot(circ_outer[0, :], circ_outer[1, :], label='Outer circle ($R = 5$)')
plt.plot(circ_aux[0, :], circ_aux[1, :], '--', color='gray', label='Construction circle (diameter $OP$)')

plt.plot(x_PA[0, :], x_PA[1, :], 'b', label=f'Tangent $PA = {PA_len:.2f}\\text{{ cm}}$')
plt.plot(x_PB[0, :], x_PB[1, :], 'b', label='Tangent $PB$')
plt.plot(x_OA[0, :], x_OA[1, :], 'k--', label='Radius $OA, OB$')
plt.plot(x_OB[0, :], x_OB[1, :], 'k--')
plt.plot(x_OP[0, :], x_OP[1, :], 'k:', label='Line $OP$')

# Scatter and label points
points = np.vstack((O, P, A, B, M)).T
plt.scatter(points[0, :], points[1, :], color='red', zorder=5)

labels = ['$O$', '$P$', '$A$', '$B$', '$M$']
offsets = [(-15, -15), (8, 5), (-15, 8), (-15, -15), (5, 5)]

for i, txt in enumerate(labels):
    plt.annotate(
        txt,
        (points[0, i], points[1, i]),
        textcoords="offset points",
        xytext=offsets[i],
        fontsize=10
    )

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
plt.grid(True)
plt.legend(loc='upper right')

plt.savefig('q36.png', dpi=300, bbox_inches='tight')
# subprocess.run(["sh", "-c", "echo 'Saved plot'"])
plt.show()
