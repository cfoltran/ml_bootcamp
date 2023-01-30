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

    def T(self):
        t = Matrix(self.shape[::-1])
        for i in range(t.shape[0]):
            for j in range(t.shape[1]):
                t.data[i][j] = self.data[j][i]
        return t

    def __add__(self, matrix):
        # if (isinstance(matrix, Matrix)):
        #     raise ValueError("Value error: one of the sum term is not a Matrix instance")
        if (self.shape != matrix.shape):
            raise ArithmeticError("Matrix have different shape")
        try:
            result = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.data[i][j] = self.data[i][j] + matrix.data[i][j]
            return result
        except:
            raise AttributeError("sum error")


    def __radd__(self, matrix):
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

    def __sub__(self, matrix):
        # if (isinstance(matrix, Matrix)):
        #     raise ValueError("Value error: one of the sum term is not a Matrix instance")
        if (self.shape != matrix.shape):
            raise ArithmeticError("Matrix have different shape")
        try:
            result = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.data[i][j] = self.data[i][j] - matrix.data[i][j]
            return result
        except:
            raise AttributeError("sum error")

    def __mul__(self, rterm):
        try:
            if isinstance(rterm, (int, float)):
                result = Matrix(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        result.data[i][j] += self.data[i][j] * rterm
                return result
            if self.shape[1] != rterm.shape[0]:
                raise ArithmeticError("Shape are not aligned")
            result = Matrix((self.shape[0], rterm.shape[1]))
            for i in range(self.shape[0]):
                for j in range(rterm.shape[1]):
                    for k in range(rterm.shape[0]):
                        result.data[i][j] += self.data[i][k] * rterm.data[k][j]
                        
            return result
        except:
            raise AttributeError("sum error")

    def __rmul__(self, rterm):
        try:
            if isinstance(rterm, (int, float)):
                result = Matrix(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        result.data[i][j] += rterm * self.data[i][j]
                return result
            if self.shape[1] != rterm.shape[0]:
                raise ArithmeticError("Shape are not aligned")
            result = Matrix((self.shape[0], rterm.shape[1]))
            for i in range(self.shape[0]):
                for j in range(rterm.shape[1]):
                    for k in range(rterm.shape[0]):
                        result.data[i][j] += rterm.data[k][j] * self.data[i][k]
                        
            return result
        except:
            raise AttributeError("sum error")

    def __truediv__(self, rterm):
        try:
            if isinstance(rterm, (int, float)):
                result = Matrix(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        result.data[i][j] += self.data[i][j] / rterm
                return result
            if self.shape[1] != rterm.shape[0]:
                raise ArithmeticError("Shape are not aligned")
            result = Matrix((self.shape[0], rterm.shape[1]))
            for i in range(self.shape[0]):
                for j in range(rterm.shape[1]):
                    for k in range(rterm.shape[0]):
                        result.data[i][j] += self.data[i][k] / rterm.data[k][j]
                        
            return result
        except:
            raise AttributeError("sum error")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        i = 0
        r = 'Matrix(['
        for l in self.data:
            i += 1
            if (i != len(self.data)):
                r += str(l)
                r += ',\n'
            else:
                r += '\t' + str(l)
        return r
        