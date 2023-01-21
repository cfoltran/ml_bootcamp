from sys import stderr

class Matrix:
    def __init__(self, *args):
        if len(args) != 1:
            raise ValueError("One arg is expected")
        self.data = self._data_(*args)
        self.shape = self._shape_(*args)

    def _data_(self, args):
        if (isinstance(args, list)):
            return args.copy()
        matrix = []
        for _ in range(args[0]):
            matrix.append([0] * args[1])
        return matrix

    def _shape_(self, args):
        if isinstance(args, tuple):
            return args
        return (len(args), len(args[0]))

    def __add__(self, matrix):
        # if (isinstance(matrix, Matrix)):
        #     raise ValueError("Value error: one of the sum term is not a Matrix instance")
        if (self.shape != matrix.shape):
            raise ArithmeticError("Matrix have different shape")
        try:
            result = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.data[i][j] = matrix.data[i][j] + self.data[i][j]
            return result
        except:
            raise AttributeError("sum error")
