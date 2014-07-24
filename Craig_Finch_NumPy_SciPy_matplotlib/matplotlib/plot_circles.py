import numpy as np
import matplotlib.pyplot as plt

def plot_circles(center_x, center_y, radius, width):
    """Plot circles in a 2D plane.

    Args:
        center_x: iterable, x coordinates of circle centers
        center_y: iterable, y coordinates of circle centers
        radius: float or integer, circle radius
        width: size of plotting area

    Returns:
        matplotlib axes with circle patches
    """
    from matplotlib.patches import Circle

    fig = plt.figure()
    ax = fig.add_subplot(111)  # Get axes object for figure

    # Add each circle to axes
    for p in range(len(center_x)):
        ax.add_patch(Circle((center_x[p], center_y[p]), radius,
            edgecolor='black', facecolor='blue'))

    ax.set_aspect(1.0)  # Otherwise, a square won't look square

    # Draw borders of plot area
    plt.axhline(y=0, color='k')
    plt.axhline(y=width, color='k')
    plt.axvline(x=0, color='k')
    plt.axvline(x=width, color='k')

    plt.axis([-0.1*width, width*1.1, -0.1*width, width*1.1]) # Set view area
    plt.xlabel("x")
    plt.ylabel("y")

    return ax

# SETUP
radius = 1.0
domain_size = 20.0
num_spheres = 15

# INITIALIZE

# Providing a seed ensures that the same sequence of pseudo-random numbers will
# be generated every time. Good for debugging!
rng = np.random.RandomState(seed=1)

# Get NumPy arrays of pseudo-random numbers to represent (x,y) coordinates of
# circle centers
x = rng.uniform(0, domain_size, num_spheres)
y = rng.uniform(0, domain_size, num_spheres)

# PLOT
ax = plot_circles(x, y, radius, domain_size)
plt.show()
