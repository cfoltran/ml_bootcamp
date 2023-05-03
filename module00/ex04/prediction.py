import numpy as np

def predict_(x, theta):
    """
    Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of dimension m * 1.
    None if x and/or theta are not numpy.array.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """
    try:
        if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
            return None
        if np.any(x == 0):
            return None
        mat = np.c_[np.ones(x.shape[0]), x]
        return mat.dot(theta)
    except:
        return None
    
x = np.arange(1,6)
theta1 = np.array([[5],[3]])
print(predict_(x, theta1))