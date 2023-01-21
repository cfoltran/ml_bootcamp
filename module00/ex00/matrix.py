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
        # @todo check type
        # @todo check shape
        try:
            result = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.data[i][j] = matrix.data[i][j] + self.data[i][j]
            return result
        except:
            raise AttributeError("sum error")


if __name__ == '__main__':
    M = Matrix([[0, 1], [0, 1]])
    M2 = Matrix([[0, 1], [0, 1]])
    res = M + M2
    print(res.data)
