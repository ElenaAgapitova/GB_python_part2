from animals import Dog, Cat, Parrot, Pet


class CreateAnimal:
    __all_animal = [Dog, Cat, Parrot]

    def __new__(cls, type_animal: str, name: str, age: int, unique_property=None):
        if type_animal.title() in [item.get_type() for item in cls.__all_animal]:
            for item in cls.__all_animal:
                if type_animal.title() == item.get_type():
                    if unique_property is not None:
                        return item(name, age, unique_property)
                    else:
                        return item(name, age)
        else:
            return Pet(name, age, unique_property)


my_pet = CreateAnimal('dog', 'Мухтар', 2)
print(my_pet)
print('Имя:', my_pet.get_name())
print('Возраст:', my_pet.get_age())
print('Свойство:', my_pet.get_unique_property())
