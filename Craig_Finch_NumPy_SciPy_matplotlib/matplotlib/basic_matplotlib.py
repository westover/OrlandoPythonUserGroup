import numpy as np
import matplotlib.pyplot as plt

# arange is similar to function range, but returns NumPy array of floats
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)

# NumPy functions return NumPy arrays
cos_x = np.cos(x)
sin_x = np.sin(x)

# Demonstrate PyPlot interface to matplotlib
plt.figure()

plt.plot(x, cos_x, label='cos(x)', linewidth=2)
plt.plot(x, sin_x, label='sin(x)', linewidth=2)

plt.xlabel('x')
plt.ylabel('y')

# Display the legend, which is automatically built from line labels
plt.legend()

# Figure won't appear until we call show()
plt.show()
