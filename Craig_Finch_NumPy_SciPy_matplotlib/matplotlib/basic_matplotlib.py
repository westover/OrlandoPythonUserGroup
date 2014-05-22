import numpy as np
import scipy
import matplotlib.pyplot as plt

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
cos_x = np.cos(x)
sin_x = np.sin(x)

plt.figure()

plt.plot(x, cos_x, label='cos(x)', linewidth=2)
plt.plot(x, sin_x, label='sin(x)', linewidth=2)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.figure()

plt.show()