from animals import Dog, Cat, Parrot


class CreateAnimal:
    __all_animal = [Dog, Cat, Parrot]

    def __init__(self, type_animal: str, name: str, age: int, unique_property=None):
        if type_animal.title() in [item.get_type() for item in self.__all_animal]:
            for item in self.__all_animal:
                if type_animal.title() == item.get_type():
                    if unique_property is not None:
                        self.pet = item(name, age, unique_property)
                    else:
                        self.pet = item(name, age)
        else:
            raise ValueError


my_pet = CreateAnimal('dog', 'Мухтар', 2)
print('Тип:', my_pet.pet.get_type())
print('Имя:', my_pet.pet.get_name())
print('Возраст:', my_pet.pet.get_age())
print('Свойство:', my_pet.pet.get_unique_property())
