import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def angled_arrow(origin, angle, length, label, **kwargs):
    """Plots an arrow with a text annotation near the middle.

    Args:
        origin		tuple of (x, y) coords for start of arrow
        angle		angle of arrow (radians)
        length		length of arrow
        label		text label
        kwargs		pass keywords through to matplotlib.pyplot.arrow

    Returns:
        A tuple of (matplotlib arrow object, matplotlib text object)
    """
    # Arrow
    arrow_dx = length * np.cos(angle)
    arrow_dy = length * np.sin(angle)
    arrow = plt.arrow(x=origin[0], y=origin[1], dx=arrow_dx,
	    dy=arrow_dy, **kwargs)

    # Text label. Text location could be a lot smarter.
    cosmetic_offset = arrow_dy * 0.1
    text_x = origin[0] + arrow_dx / 2 + cosmetic_offset
    text_y = origin[1] + arrow_dy / 2 - cosmetic_offset
    fontsize = int(mpl.rcParams['font.size'] * 1.5) # 1.5*default font size
    annotation = plt.text(text_x, text_y, label, fontsize=fontsize)

    return arrow, annotation

# SETUP
radius = 1.0
center1 = (0.0, 0.0)
arrow1_angle = np.pi/4	# radians
center2 = (2 * radius * np.cos(np.pi/4), 2 * radius * np.sin(np.pi/4))
arrow2_angle = 5 * np.pi / 4	# radians

# PLOT
fig = plt.figure()
ax = fig.add_subplot(111)

# Circles
ax.add_patch(Circle(center1, radius, edgecolor='blue', facecolor='lightgray'))
ax.add_patch(Circle(center2, radius, edgecolor='red', facecolor='lightgray'))

# Arrows
arrow1 = angled_arrow(center1, arrow1_angle, radius, '$r_1$',
    length_includes_head=True, width=0.05, head_width=0.2, color='blue')
arrow2 = angled_arrow(center2, arrow2_angle, radius, '$r_2$',
    length_includes_head=True, width=0.05, head_width=0.2, color='red')

# Text annotations
# Text between $...$ is parsed through a LaTeX interpeter.
plt.text(center1[0], center1[1] - 0.2, '$(x_1, y_1)$',
    fontsize = int(mpl.rcParams['font.size'] * 1.5))
plt.text(center2[0], center2[1] + 0.1, '$(x_2, y_2)$',
    fontsize = int(mpl.rcParams['font.size'] * 1.5))

# Add formula for distance between points in a plane
plt.text(-1.25, 2.25, "$d=\sqrt{\Delta x^2 + \Delta y^2}$", fontsize=18)

ax.set_aspect(1.0)  # without this, a square will not look square
plt.axis([-1.5, 3, -1.5, 3])

plt.show()
