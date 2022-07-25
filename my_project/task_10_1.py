from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        ln = [len(i) for i in matrix]
        if ln[0] * len(ln) == sum(ln):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    def __str__(self):
        __string = str()
        for el in self.matrix:
            __string += f'\n{str(el).replace(",", " ").replace("[", "|").replace("]", "|")}'
        return __string

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Матрицы должны быть одного размера!')
        return Matrix([list(map(sum, zip(row_1, row_2)))
                       for row_1, row_2 in zip(self.matrix, other.matrix)])


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])