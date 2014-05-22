import numpy as np
import matplotlib.pyplot as plt

def plot_circles(adsorbed_x, adsorbed_y, radius, width, reference_indices=[]):
    from matplotlib.patches import Circle

    # Plot each run
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for p in range(len(adsorbed_x)):
        if len(np.where(reference_indices == p)[0]) > 0:
            ax.add_patch(Circle((adsorbed_x[p], adsorbed_y[p]), radius, 
                edgecolor='black', facecolor='black'))
        else:
            ax.add_patch(Circle((adsorbed_x[p], adsorbed_y[p]), radius,
                edgecolor='black', facecolor='blue'))

    ax.set_aspect(1.0)
    plt.axhline(y=0, color='k')
    plt.axhline(y=width, color='k')
    plt.axvline(x=0, color='k')
    plt.axvline(x=width, color='k')
    plt.axis([-0.1*width, width*1.1, -0.1*width, width*1.1])
    plt.xlabel("x")
    plt.ylabel("y")

    return ax

# SETUP
radius = 1.0
domain_size = 20.0
num_spheres = 15

# INITIALIZE
rng = np.random.RandomState(seed=1)

x = rng.uniform(0, domain_size, num_spheres)
y = rng.uniform(0, domain_size, num_spheres)

# PLOT
ax = plot_circles(x, y, radius, domain_size)
plt.show()