from functools import total_ordering


class NegativeValueError(Exception):
    pass


@total_ordering
class Rectangle:
    """
    Класс прямоугольник
    """

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        if height is None:
            height = width
        if height <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __add__(self, other):
        """Сложение сторон прямоугольника и создание нового объекта"""
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, float(self.height + other.height))
        raise TypeError

    def __sub__(self, other):
        """Вычитание сторон прямоугольника и создание нового объекта"""
        if isinstance(other, Rectangle):
            if self.width > other.width and self.height > other.height:
                return Rectangle(self.width - other.width, float(self.height - other.height))
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


if __name__ == '__main__':
    # rect1 = Rectangle(4, 5)
    # rect2 = Rectangle(-5, 3)

    # rect3 = Rectangle(4, -5)
    r = Rectangle(5, -3)
    # rect1.width = -3
    # rect1.height = -4
