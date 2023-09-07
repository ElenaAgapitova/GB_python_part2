#  Напишите функцию для транспонирования матрицы


my_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def matrix_transposition_zip(matrix: list[list[int]]) -> list[list[int]]:
    """
    Функция транспонирования матрицы с помощью функции zip.
    :param matrix: двухмерный список для транспонирования.
    :return: двухмерный список, в котором столбцы исходной матрицы становятся строками результирующей.
    """
    return [list(item) for item in zip(*matrix)]


def matrix_transposition_loop(matrix: list[list[int]]) -> list[list[int]]:
    """
    Функция транспонирования матрицы с циклами.
    :param matrix: двухмерный список для транспонирования.
    :return: двухмерный список, в котором столбцы исходной матрицы становятся строками результирующей.
    """
    transposed_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


def print_matrix(text: str, matrix: list[list[int]]) -> None:
    print(text)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t')
        print()
    print()


print_matrix('Исходная матрица:', my_matrix)
print_matrix('Транспонированная матрица функцией №1 (zip):', matrix_transposition_zip(my_matrix))
print_matrix('Транспонированная матрица функцией №2 (цикл):', matrix_transposition_loop(my_matrix))
