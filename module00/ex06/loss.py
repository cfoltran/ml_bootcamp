import numpy as np


def predict_(x, theta):
    try:
        # if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        #     return None
        # if np.any(x == 0):
        #     return None
        mat = np.c_[np.ones(x.shape[0]), x]
        return mat.dot(theta)
    except:
        return None

def loss_elem_(y, y_hat):
    """
    Description:
        Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
        y: has to be an numpy.array, a vector.
        y_hat: has to be an numpy.array, a vector.
    Returns:
        J_elem: numpy.array, a vector of dimension (number of the training examples,1).
        None if there is a dimension matching problem between X, Y or theta.
        None if any argument is not of the expected type.
    Raises:
        This function should not raise any Exception.
    """
    try:
        res = np.zeros(y.shape[0])
        for i in range(y.shape[0]):
            res[i] = (y_hat[i] - y[i]) ** 2
        return res
    except:
        return None

def loss_(y, y_hat):
    """
    Description:
        Calculates the value of loss function.
    Args:
        y: has to be an numpy.array, a vector.
        y_hat: has to be an numpy.array, a vector.
    Returns:
        J_value : has to be a float.
        None if there is a dimension matching problem between X, Y or theta.
        None if any argument is not of the expected type.
    Raises:
        This function should not raise any Exception.
    """
    try:
        return np.sum(loss_elem_(y, y_hat))
    except:
        return None


x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print(loss_elem_(y1, y_hat1))
