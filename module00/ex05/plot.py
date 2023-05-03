import matplotlib.pyplot as plt
import numpy as np

def plot(x, y, theta):
    """
    Plot the data and prediction line from three non-empty numpy.array.
    Args:
        x: has to be an numpy.array, a vector of dimension m * 1.
        y: has to be an numpy.array, a vector of dimension m * 1.
        theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
        This function should not raise any Exceptions.
    """
    try:
        plt.plot(x, y, 'o')
        plt.plot(x, theta[0] + theta[1] * x)
        plt.show()
    except:
        return None


x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
theta1 = np.array([[4.5],[-0.2]])
plot(x, y, theta1)