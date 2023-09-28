class Triangle:

    def __init__(self, a: float, b: float, c: float):
        if self.__check_triangle(a, b, c):
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise ValueError

    @staticmethod
    def __check_triangle(a, b, c):
        if (a + b) < c or \
                (a + c) < b or (c + b) < a or \
                (a == 0 or b == 0 or c == 0):
            return False
        return True

    def get_sides(self):
        return f'side a = {self.__a}, side b = {self.__b}, side c = {self.__c}'


triangle_1 = Triangle(3, 4, 5)
print(triangle_1.get_sides())  # side a = 3, side b = 4, side c = 5

triangle_2 = Triangle(1, 2, 4)  # raise ValueError
print(triangle_2.get_sides())

triangle_3 = Triangle(3, 0, 5)  # raise ValueError
print(triangle_1.get_sides())
