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

    def _shape_(self, args):
        return (len(args), len(args[0]))



if __name__ == '__main__':
    M = Matrix([[0, 1], [2, 3], [4, 5]])
    print(M.shape)
