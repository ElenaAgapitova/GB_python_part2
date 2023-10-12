class CheckName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.__validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def __validate(value: str):
        if not isinstance(value, str):
            raise TypeError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        for char in value:
            if not char.isalpha() and not char.isspace():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        if not value.istitle():
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')


class CheckLevel:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.__validate(value)
        setattr(instance, self.param_name, value)

    def __validate(self, value):
        if value < self.min_value or value > self.max_value:
            raise ValueError(f'Значение должно быть целым числом от {self.min_value} '
                             f'до {self.max_value}')


class CheckId:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.__validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def __validate(value: str):
        if len(value) != 6:
            raise ValueError('ID должен состоять из 6 цифр')
        if not value.isdigit():
            raise ValueError('ID должен состоять из 6 цифр')


class Employee:
    name = CheckName()
    lvl_access = CheckLevel(1, 7)
    employee_id = CheckId()

    def __init__(self, name: str, lvl_access: int | str, employee_id: str):
        self.name = name
        self.lvl_access = int(lvl_access)
        self.employee_id = employee_id

    def __str__(self):
        return f'{self.name} ({self.employee_id}) | Доступ: {self.lvl_access}'

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.employee_id == other.employee_id
        else:
            raise ValueError('Недопустимая операция')
