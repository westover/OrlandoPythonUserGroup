import numpy as np

def timer(func):
    """Decorator to calculate the run time of a function."""
    import time

    def st_func(*args, **keyArgs):
        t1 = time.time()
        r = func(*args, **keyArgs)
        t2 = time.time()
        print("Function={}, Time={} sec".format(func.__name__, t2 - t1))
        return r

    return st_func

@timer
def find_distances_1(x, y, z, radius):
    """Find distances between all particles. Naive implementation.
    Args:
    x, y, z     NumPy arrays
    Returns:
    d       2D NumPy array of center-center distances
    """

    assert len(x) == len(y) == len(z)
    d = np.array(np.zeros((len(x), len(x))))
    # Don't do it like this!
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
    x, y, z     NumPy arrays
    Returns:
    d       2D NumPy array of center-center distances
    """

    assert len(x) == len(y) == len(z)
    d = np.array(np.zeros((len(x), len(x))))
    for i in range(len(x)):
        # Remove "if" from inner loop
        # Eliminate redundant calculations
        for j in range(i):
	    d[i, j] = np.sqrt( (x[i] - x[j])**2 + (y[i] - y[j])**2 \
                + (z[i] - z[j])**2 ) - 2 * radius
    return d

@timer
def find_distances_3(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation.
    Args:
    x, y, z     NumPy arrays
    Returns:
    d       2D NumPy array of center-center distances
    """

    assert len(x) == len(y) == len(z)
    d = np.array(np.zeros((len(x), len(x))))
    for i in range(len(x)):
        # Vectorized inner loop
        d[i, :] = np.sqrt((x[i] - x)**2 + (y[i] - y)**2 + (z[i] - z)**2) - 2 * radius
    return d

@timer
def find_distances_4(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation 2.
    Args:
    x, y, z     NumPy arrays
    Returns:
    d       2D NumPy array of center-center distances
    """

    assert len(x) == len(y) == len(z)
    d = np.array(np.zeros((len(x), len(x))))
    for i in range(len(x)):
        # Moved square root out of inner loop
        d[i, :] = (x[i] - x)**2 + (y[i] - y)**2 + (z[i] - z)**2
    return np.sqrt(d) - 2 * radius

@timer
def find_distances_5(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation 3.
    Args:
    x, y, z     NumPy arrays
    Returns:
    d       2D NumPy array of center-center distances
    """

    assert len(x) == len(y) == len(z)
    d = np.array(np.zeros((len(x), len(x))))
    for i in range(len(x)):
        # Eliminating redundant calculations from vectorized inner loop
        d[i, :i] = np.sqrt((x[i] - x[:i])**2 + (y[i] - y[:i])**2 \
            + (z[i] - z[:i])**2) - 2 * radius
    return d

@timer
def find_distances_6(x, y, z, radius):
    """Find distances between all particles. Vectorized implementation 4.
    Args:
    x, y, z     NumPy arrays
    Returns:
    d       2D NumPy array of center-center distances
    """

    assert len(x) == len(y) == len(z)
    d = np.array(np.zeros((len(x), len(x))))
    for i in range(len(x)):
        # trying np.power() instead of ** operator
        d[i, :i] = np.sqrt( np.power((x[i] - x[:i]),2) \
            + np.power((y[i] - y[:i]),2) + np.power((z[i] - z[:i]), 2)) \
            - 2 * radius
    return d

