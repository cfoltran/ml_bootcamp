import matrix
import unittest

def basicMatrix():
    expected = [[0, 0], [0, 0]]
    M = matrix.Matrix(expected)
    log(M)


if __name__ == '__main__':
    unittest.main()