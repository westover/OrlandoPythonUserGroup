import os
import numpy as np
from distance import *

# This example shows how a distance-finding routine to determine which
# spheres in the set collide (overlap)

# SETUP
radius = 1.0
domain_size = 4.0
num_spheres = 5

# INITIALIZE
# Set random seed so same pseudo-random numbers are used for every run
rng = np.random.RandomState(seed=1)

x = rng.uniform(0, domain_size, num_spheres)
y = rng.uniform(0, domain_size, num_spheres)
z = rng.uniform(0, domain_size, num_spheres)

# RUN
d = find_distances_5(x, y, z, radius)
print(os.linesep + "Matrix of distances between spheres:")
print(d)

# Spheres with edge-edge distance < 0 collide (overlap)
print(os.linesep + "Overlap matrix:")
print(d < 0.0)

# Identify indices of colliding (overlapping) spheres
collisions = np.where(d < 0.0)
print(os.linesep + "Indices of spheres that overlap:")
print(collisions)

# Reformat as a list of tuples
collision_indices = zip(collisions[0], collisions[1])
print(os.linesep + "Indices of spheres that overlap (as a list of tuples):")
print(collision_indices)

