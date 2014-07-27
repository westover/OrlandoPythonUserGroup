"""Functions for computing all distances between a set of spheres.

The purpose of these functions is to illustrate the effect of various
performance optimizations for numerical Python code.
"""

import numpy as np

def timer(func):
    """Decorator to calculate the run time of a function."""
    from functools import wraps
    import time

    @wraps(func)  # allows PyDoc to find docstrings of decorated functions
    def st_func(*args, **keyArgs):
        t1 = time.time()
        r = func(*args, **keyArgs)
        t2 = time.time()
        print("Function={}, Time={} sec".format(func.__name__, t2 - t1))
        return r

    return st_func

def find_distances_1(x, y, z, radius):
    """Find distances between all particles. Naive implementation.

    Args:
        x: NumPy array of particle x coordinates
        y: NumPy array of particle y coordinates
        z: NumPy array of particle z coordinates

    Returns:
        2D NumPy array of center-center distances
    """
    assert len(x) == len(y) == len(z)  # primitive input validation

    d = np.zeros((len(x), len(x)))  # center-center distances

    # This algorithm is NOT efficient
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                d[i, j] = np.sqrt( (x[i] - x[j])**2 + (y[i] - y[j])**2 \
                    + (z[i] - z[j])**2 ) - 2 * radius
            else:
                d[i, j] = 0.0
    return d

@timer
def find_distances_2(x, y, z, radius):
    """Find distances between all particles. Less naive implementation.

    Args:
        x: NumPy array of particle x coordinates
        y: NumPy array of particle y coordinates
        z: NumPy array of particle z coordinates

    Returns:
        2D NumPy array of center-center distances
    """
    assert len(x) == len(y) == len(z)  # primitive input validation

    d = np.zeros((len(x), len(x)))  # center-center distances

    # Remove "if" from inner loop and eliminate redundant calculations
    for i in range(len(x)):
        for j in range(i):
	    d[i, j] = np.sqrt( (x[i] - x[j])**2 + (y[i] - y[j])**2 \
                + (z[i] - z[j])**2 ) - 2 * radius
    return d

@timer
def find_distances_3(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation.

    Args:
        x: NumPy array of particle x coordinates
        y: NumPy array of particle y coordinates
        z: NumPy array of particle z coordinates

    Returns:
        2D NumPy array of center-center distances
    """
    assert len(x) == len(y) == len(z)  # primitive input validation

    d = np.zeros((len(x), len(x)))  # center-center distances

    for i in range(len(x)):
        # Vectorized inner loop
        d[i, :] = np.sqrt((x[i] - x)**2 + (y[i] - y)**2 + (z[i] - z)**2) - 2 * radius
    return d

@timer
def find_distances_4(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation 2.

    Args:
        x: NumPy array of particle x coordinates
        y: NumPy array of particle y coordinates
        z: NumPy array of particle z coordinates

    Returns:
        2D NumPy array of center-center distances
    """
    assert len(x) == len(y) == len(z)  # primitive input validation

    d = np.zeros((len(x), len(x)))  # center-center distances

    # Moved square root out of inner loop
    for i in range(len(x)):
        d[i, :] = (x[i] - x)**2 + (y[i] - y)**2 + (z[i] - z)**2
    return np.sqrt(d) - 2 * radius

@timer
def find_distances_5(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation 3.

    Args:
        x: NumPy array of particle x coordinates
        y: NumPy array of particle y coordinates
        z: NumPy array of particle z coordinates

    Returns:
        2D NumPy array of center-center distances
    """
    assert len(x) == len(y) == len(z)  # primitive input validation

    d = np.zeros((len(x), len(x)))  # center-center distances

    # Eliminating redundant calculations from vectorized inner loop
    for i in range(len(x)):
        d[i, :i] = np.sqrt((x[i] - x[:i])**2 + (y[i] - y[:i])**2 \
            + (z[i] - z[:i])**2) - 2 * radius
    return d

@timer
def find_distances_6(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation 3.

    Args:
        x: NumPy array of particle x coordinates
        y: NumPy array of particle y coordinates
        z: NumPy array of particle z coordinates

    Returns:
        2D NumPy array of center-center distances
    """
    assert len(x) == len(y) == len(z)  # primitive input validation

    d = np.zeros((len(x), len(x)))  # center-center distances

    # Trying np.power() instead of ** operator
    for i in range(len(x)):
        d[i, :i] = np.sqrt( np.power((x[i] - x[:i]),2) \
            + np.power((y[i] - y[:i]),2) + np.power((z[i] - z[:i]), 2)) \
            - 2 * radius
    return d

