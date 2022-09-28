import random
import math

class Matrix:
    def __init__(self, x, y):
        self.matrx = self.get_matrix(x, y)

    @staticmethod
    def get_matrix(x, y):
        matrix = [[i for i in range(y)] for _ in range(x)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num = random.randint(1, 99)
                matrix[i][j] = num
        return matrix

    @staticmethod
    def readable_matrix(matrix):
        new_matrix = []
        for row in matrix:
            print(row)
        return '\n'.join(new_matrix)

    def get_element(self, i, j):
        return self.matrx[i - 1][j - 1]

    def set_element(self, i, j, value):
        modified = self.matrx[i - 1][j - 1] = value
        return modified

    def transpose(self):
        transposed = [[self.matrx[j][i] for j in range(len(self.matrx))]
                      for i in range(len(self.matrx[0]))]
        return self.readable_matrix(transposed)

    def __str__(self):
        return f"{self.readable_matrix(self.matrx)}"

    def __len__(self):
        return len(self.matrx)

    def __getitem__(self, item):
        return self.matrx[item]

    def multiply(self, matrix):
        result = [[0 for _ in range(len(matrix[i]))] for i in range(len(self.matrx))]
        for i in range(len(self.matrx)):
            for j in range(len(matrix[0])):
                for k in range(len(matrix)):
                    result[i][j] += self.matrx[i][k] * matrix[k][j]
        return self.readable_matrix(result)

    def __mul__(self, scalar):
        if isinstance(scalar, Matrix):
            return self.readable_matrix(self.multiply(scalar))
        return self.readable_matrix([[num * scalar for num in row] for row in self.matrx])


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


