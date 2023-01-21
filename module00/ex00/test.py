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

    def test_sumShapeError(self):
        with self.assertRaises(ArithmeticError):
            m1 = matrix.Matrix([[2, 3, 4], [2, 3, 4]])
            m2 = matrix.Matrix([[2, 3], [2, 3]])
            m = m1 + m2
        

if __name__ == '__main__': 
    unittest.main()