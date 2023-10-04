class Matrix:

    def __init__(self, rows: int, columns: int, numbers: list[int]):
        if len(numbers) == rows * columns:
            m = 0
            matrix = [[0 for _ in range(columns)] for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    matrix[i][j] = numbers[m]
                    m += 1
            self.__matrix = matrix
        else:
            raise ValueError

    def transposition(self):
        self.__matrix = [list(item) for item in zip(*self.__matrix)]

    def __str__(self):
        text_matrix = ''
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                text_matrix += str(self.__matrix[i][j]) + '\t'
            text_matrix += '\n'
        text_matrix += '\n'
        return text_matrix


matrix_1 = Matrix(3, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(matrix_1)
matrix_1.transposition()
print(matrix_1)
