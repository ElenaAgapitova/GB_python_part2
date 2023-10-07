class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, id_):
        self.id_ = id_

    def __str__(self):
        return f'Invalid id: {self.id_}. Id should be a 6-digit positive integer between ' \
               f'100000 and 999999.'


class Person:

    def __init__(self, first_name: str, middle_name: str, last_name: str, age: int):
        if first_name == '':
            raise InvalidNameError(first_name)
        if middle_name == '':
            raise InvalidNameError(middle_name)
        if last_name == '':
            raise InvalidNameError(last_name)
        if age < 0 and not isinstance(age, int):
            raise InvalidAgeError(age)
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, first_name: str, middle_name: str, last_name: str, age: int, id_: int):
        super().__init__(first_name, middle_name, last_name, age)
        self.__validation(id_)
        self.id_ = id_

    def get_level(self):
        return sum([int(item) for item in str(self.id_)]) % 7

    @staticmethod
    def __validation(value):
        if not isinstance(value, int) or len(str(value)) < 6 or value < 0:
            raise InvalidIdError(value)
