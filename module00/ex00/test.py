import matrix
import unittest
import sys
import numpy as np

class MatrixSum(unittest.TestCase):
    def test_sum2x2(self):
        m1 = matrix.Matrix([[2, 3], [4, 5]])
        m2 = matrix.Matrix([[4, 6], [7, 8]])
        m = m1 + m2
        self.assertEqual(m.data, [[6, 9], [11, 13]])

    def test_shape_errors(self):
        m1 = matrix.Matrix([[2, 3, 4], [2, 3, 4]])
        m2 = matrix.Matrix([[2, 3], [2, 3]])
        with self.assertRaises(ArithmeticError):
            m = m1 + m2
        with self.assertRaises(ArithmeticError):
            m = m1 - m2


    def test_sum4x4(self):
        m1 = matrix.Matrix([[2, 3], [4, 5]])
        m2 = matrix.Matrix([[4, 6], [7, 8]])
        m = m1 - m2
        self.assertEqual(m.data, [[-2, -3], [-3, -3]])

    def test_mul_int(self):
        m1 = matrix.Matrix([[2, 3], [4, 5]])
        res = m1 * 2
        self.assertEqual(res.data, [[4, 6], [8, 10]])
    
    def test_mul_matrix(self):
        m1 = matrix.Matrix([[3, 4, 5], [6, 2, 1]])
        m2 = matrix.Matrix([[1, 1], [1, 1], [1, 1]])
        res = m1 * m2
        self.assertEqual(res.data, [[12, 12], [9, 9]])

    # def test_mul_invalid_shape(self):
    #     m1 = matrix.Matrix([[3, 4, 5, 5]])
    #     m2 = matrix.Matrix([[1, 1], [1, 1], [1, 1]])
    #     with self.assertRaises(ArithmeticError):
    #         m = m1 * m2
            

    def test_rmul_matrix(self):
        m1 = matrix.Matrix([[3, 4, 5], [6, 2, 1]])
        m2 = matrix.Matrix([[1, 1], [1, 1], [1, 1]])
        res = m1.__rmul__(m2);
        print(res.data)
        # self.assertEqual(res.data, [[12, 12], [9, 9]])

if __name__ == '__main__': 
    unittest.main()