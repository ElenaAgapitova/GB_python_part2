class Matrix:

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def __add__(self, other):
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
            my_matrix = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    new_matrix[i][j] = self.data[i][j] + other.data[i][j]
            my_matrix.data = new_matrix
            return my_matrix
        else:
            raise ValueError

    def __mul__(self, other):
        new_matrix = [[0 for _ in range(other.columns)] for _ in range(self.rows)]
        if isinstance(other, Matrix) and self.columns == other.rows:
            my_matrix = Matrix(other.columns, self.rows)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        new_matrix[i][j] += self.data[i][k] * other.data[k][j]
            my_matrix.data = new_matrix
            return my_matrix
        else:
            raise ValueError

    def __eq__(self, other):
        new_matrix = [[0 for _ in range(other.columns)] for _ in range(self.rows)]
        if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    new_matrix[i][j] = self.data[i][j] - other.data[i][j]
                    if new_matrix[i][j] != 0:
                        return False
            return True
        else:
            return False

    def __str__(self):
        text_matrix = ''
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                text_matrix += str(self.data[i][j]) + ' '
            text_matrix += '\n'
        return text_matrix[:len(text_matrix) - 1]


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
