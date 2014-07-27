import numpy as np
from distance import *

# SETUP
radius = 1.0
domain_size = 5.0
num_spheres = 5
delta = 1e-6	# tolerance for checking whether matrices are "identical"

# Set random seed so same pseudo-random numbers are used for every run
rng = np.random.RandomState(seed=1)

x = rng.uniform(0, domain_size, num_spheres)
y = rng.uniform(0, domain_size, num_spheres)
z = rng.uniform(0, domain_size, num_spheres)

# Make sure all routines return the same result
d1 = find_distances_1(x, y, z, radius)
d2 = find_distances_2(x, y, z, radius)
d3 = find_distances_3(x, y, z, radius)
d4 = find_distances_4(x, y, z, radius)
d5 = find_distances_5(x, y, z, radius)
d6 = find_distances_6(x, y, z, radius)

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)

# Idea for unit-testing floating point code with NumPy

# Use np.tril to return lower triangle of each 2D array, since the values on
# the diagonal and upper triangle will vary between algorithms
assert(np.max(abs(np.tril(d1, k=-1) - np.tril(d2, k=-1))) < delta)
assert(np.max(abs(np.tril(d1, k=-1) - np.tril(d3, k=-1))) < delta)
assert(np.max(abs(np.tril(d1, k=-1) - np.tril(d4, k=-1))) < delta)
assert(np.max(abs(np.tril(d1, k=-1) - np.tril(d5, k=-1))) < delta)
assert(np.max(abs(np.tril(d1, k=-1) - np.tril(d6, k=-1))) < delta)
