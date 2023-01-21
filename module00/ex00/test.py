import matrix
import unittest
import sys

class MatrixSum(unittest.TestCase):
    def test_sum2x2(self):
        m1 = matrix.Matrix([[2, 3], [4, 5]])
        m2 = matrix.Matrix([[4, 6], [7, 8]])
        m = m1 + m2
        print(m.data)
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
        

if __name__ == '__main__': 
    unittest.main()