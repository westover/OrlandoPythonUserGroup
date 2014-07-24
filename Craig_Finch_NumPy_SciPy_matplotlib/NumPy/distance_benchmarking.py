import numpy as np
import cProfile
from distance import *

# SETUP
radius = 1.0
domain_size = 50.0
num_spheres = 1000

# Benchmark non-vectorized versions
print("Benchmarking with 1000 particles.")
rng = np.random.RandomState(seed=1)

x = rng.uniform(0, domain_size, num_spheres)
y = rng.uniform(0, domain_size, num_spheres)
z = rng.uniform(0, domain_size, num_spheres)

find_distances_1(x, y, z, radius)
find_distances_2(x, y, z, radius)
find_distances_3(x, y, z, radius)

# Benchmark vectorized codes
print("Benchmarking with 3000 particles.")

num_spheres = 3000

rng = np.random.RandomState(seed=1)

x = rng.uniform(0, domain_size, num_spheres)
y = rng.uniform(0, domain_size, num_spheres)
z = rng.uniform(0, domain_size, num_spheres)

find_distances_3(x, y, z, radius)
find_distances_4(x, y, z, radius)
find_distances_5(x, y, z, radius)
find_distances_6(x, y, z, radius)

#cProfile.run('find_distances_1(x, y, z, radius)')
#cProfile.run('find_distances_2(x, y, z, radius)')
#cProfile.run('find_distances_3(x, y, z, radius)')
#cProfile.run('find_distances_4(x, y, z, radius)')
#cProfile.run('find_distances_5(x, y, z, radius)')
#cProfile.run('find_distances_6(x, y, z, radius)')
