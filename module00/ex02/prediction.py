import numpy as np

def simple_predict(x, theta):
    """
    Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    try:
        if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
            return None
        if theta.shape != (2,) or len(x.shape) != 1:
            return None
        y = np.zeros(x.shape[0])
        for i in range(x.shape[0]):
            y[i] = theta[0] + theta[1] * x[i]
        return y
    except:
        return None
    

x = np.arange(1,6)
theta1 = np.array([5, 3])
print(simple_predict(x, theta1))
