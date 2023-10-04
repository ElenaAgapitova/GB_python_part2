from functools import total_ordering


@total_ordering
class Rectangle:
    """
    Класс прямоугольник
    """

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return self.a + self.b

    def __add__(self, other):
        """Сложение сторон прямоугольника и создание нового объекта"""
        if isinstance(other, Rectangle):
            return Rectangle(self.a + other.a, self.b + other.b)
        raise TypeError

    def __sub__(self, other):
        """Вычитание сторон прямоугольника и создание нового объекта"""
        if isinstance(other, Rectangle):
            if self.a > other.a and self.b > other.b:
                return Rectangle(self.a - other.a, self.b - other.b)
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами ({self.a}, {self.b})'


rect_1 = Rectangle(8, 15)
rect_2 = Rectangle(7, 14)
print(rect_1 - rect_2)
print(rect_1 + rect_2)
print(rect_1 < rect_2)
print(rect_1 == rect_2)
print(rect_1 > rect_2)
print(rect_1 != rect_2)
print(rect_1 >= rect_2)
print(rect_1 <= rect_2)
