from typing import Union


class InvalidError(Exception):
    pass


class InvalidTextError(InvalidError):
    pass


class InvalidNumberError(InvalidError):
    pass


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, text: str, number: Union[int, float]):
        if text == '' or not isinstance(text, str):
            raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        if number < 0:
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


if __name__ == '__main__':
    # invalid_archive_instance = Archive("", -5)
    # print(invalid_archive_instance)

    invalid_archive_instance = Archive("Sample text", -5)
    print(invalid_archive_instance)
