import copy


class Archive:
    archive_text = []
    archive_number = []
    instance = None

    def __new__(cls, *args):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, text: str, number: int | float):
        self.text = text
        self.number = number
        self.archive_text = copy.deepcopy(self.__class__.archive_text)
        self.__class__.archive_text.append(self.text)
        self.archive_number = copy.deepcopy(self.__class__.archive_number)
        self.__class__.archive_number.append(self.number)

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. ' \
               f'Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"


archive1 = Archive("First Text", 1)

print(archive1)

archive2 = Archive("Second Text", 2)

print(archive2)

archive3 = Archive("Third Text", 3)

print(archive1)
print(archive3)

print(archive1.archive_text)  # Выведет: ['First Text', 'Third Text']
print(archive1.archive_number)  # Выведет: [1, 3]
print(archive2.archive_text)  # Выведет: ['First Text', 'Second Text']
print(archive2.archive_number)

