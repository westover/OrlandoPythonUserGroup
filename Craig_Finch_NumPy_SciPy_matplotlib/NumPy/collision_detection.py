import numpy as np
from distance import *

# In this example, we use our distance-finding routine to determine which
# spheres collide (overlap)

# SETUP
radius = 1.0
domain_size = 4.0
num_spheres = 5

# INITIALIZE
rng = np.random.RandomState(seed=1)

x = rng.uniform(0, domain_size, num_spheres)
y = rng.uniform(0, domain_size, num_spheres)
z = rng.uniform(0, domain_size, num_spheres)

# RUN
d = find_distances_5(x, y, z, radius)
print(d)

# Spheres with edge-edge distance < 0 collide (overlap)
print(d < 0.0)

# Identify indices of colliding spheres
collisions = np.where(d < 0.0)
print(collisions)

# Reformat as a list of tuples
collision_indices = zip(collisions[0], collisions[1])
print(collision_indices)

