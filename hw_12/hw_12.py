import csv


class Number:
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
        if not isinstance(value, int):
            raise TypeError(f'Оценка должна быть целым числом от {self.min_value} до {self.max_value}')
        if value < self.min_value or value > self.max_value:
            raise ValueError(f'Оценка должна быть целым числом от {self.min_value} до {self.max_value}')


class Text:

    def __set_name__(self, owner, name):
        self.param_name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.__validate(value)
        setattr(instance, self.param_name, value)

    @staticmethod
    def __validate(value):
        if not isinstance(value, str):
            raise TypeError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        for char in value:
            if not char.isalpha() and not char.isspace():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        if not value.istitle():
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Student:
    __grade = Number(2, 5)
    __test_score = Number(0, 100)
    __std_name = Text()

    def __init__(self, name, subjects_file: str):
        self.__std_name = name
        self._subject = {}
        with open(subjects_file, 'r') as file:
            lines = csv.reader(file, dialect='excel')
            for line in lines:
                for item in line:
                    self._subject[item] = {'grade': [], 'test_score': []}

    def add_grade(self, subject, grade):
        if subject not in self._subject.keys():
            self._subject[subject] = {'grades': [], 'test_scores': []}
        self.__grade = grade
        self._subject[subject]['grade'].append(self.__grade)

    def add_test_score(self, subject, test_score):
        if subject not in self._subject.keys():
            self._subject[subject] = {'grades': [], 'test_scores': []}
        self.__test_score = test_score
        self._subject[subject]['test_score'].append(self.__test_score)

    def get_average_grade(self, subject=None):
        total_sum = 0
        count = 0
        if subject is not None and subject not in self._subject.keys():
            raise ValueError(f'Предмет {subject} не найден')
        if not subject:
            for item in self._subject.values():
                total_sum += sum(item['grade'])
                count += len(item['grade'])
        else:
            total_sum = sum(self._subject[subject]['grade'])
            count = len(self._subject[subject]['grade'])
        return total_sum / count if count != 0 else 0

    def get_average_test_score(self, subject):
        total_sum = 0
        count = 0
        if subject is not None and subject not in self._subject.keys():
            raise ValueError(f'Предмет {subject} не найден')
        if not subject:
            for item in self._subject.values():
                total_sum += sum(item['test_score'])
                count += len(item['test_score'])
        else:
            total_sum = sum(self._subject[subject]['test_score'])
            count = len(self._subject[subject]['test_score'])
        return total_sum / count if count != 0 else 0

    def get_subject(self):
        text = []
        for key in self._subject.keys():
            if len(self._subject[key]['grade']) > 0 or len(self._subject[key]['test_score']):
                text.append(key)
        return f'Предметы: {", ".join(text)}'

    def __str__(self):
        return f'Студент: {self.__std_name}\n{self.get_subject()}'


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

# student = Student("123 Иван", "subjects.csv")
