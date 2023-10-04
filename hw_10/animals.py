class Pet:
    def __init__(self, name: str, age: int, unique_property=None):
        self.__name = name
        self.__age = age
        self.__unique_property = unique_property

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_unique_property(self):
        if self.__unique_property:
            return self.__unique_property


class Dog(Pet):
    __type_animal = 'Dog'

    def __init__(self, name, age, unique_property='лает и кусает, в дом не пускает:)'):
        super().__init__(name, age, unique_property)

    @classmethod
    def get_type(cls):
        return cls.__type_animal


class Cat(Pet):
    __type_animal = 'Cat'

    def __init__(self, name, age, unique_property='мурлыкает'):
        super().__init__(name, age, unique_property)

    @classmethod
    def get_type(cls):
        return cls.__type_animal


class Parrot(Pet):
    __type_animal = 'Parrot'

    def __init__(self, name, age, unique_property='говорит'):
        super().__init__(name, age, unique_property)

    @classmethod
    def get_type(cls):
        return cls.__type_animal
