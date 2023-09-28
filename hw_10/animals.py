from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def get_unique_property(self):
        """Возвращает уникальное свойство"""


class Dog(Pet):
    __type_animal = 'Dog'

    def __init__(self, name, age, unique_property='лает и кусает, в дом не пускает:)'):
        super().__init__(name, age)
        self.__unique_property = unique_property

    @classmethod
    def get_type(cls):
        return cls.__type_animal

    def get_unique_property(self):
        return self.__unique_property


class Cat(Pet):
    __type_animal = 'Cat'

    def __init__(self, name, age, unique_property='мурлыкает'):
        super().__init__(name, age)
        self.__unique_property = unique_property

    @classmethod
    def get_type(cls):
        return cls.__type_animal

    def get_unique_property(self):
        return self.__unique_property


class Parrot(Pet):
    __type_animal = 'Parrot'

    def __init__(self, name, age, unique_property='говорит'):
        super().__init__(name, age)
        self.__unique_property = unique_property

    @classmethod
    def get_type(cls):
        return cls.__type_animal

    def get_unique_property(self):
        return self.__unique_property
