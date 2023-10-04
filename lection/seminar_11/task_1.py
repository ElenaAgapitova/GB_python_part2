"""
📌Создайте класс Архив, который хранит пару свойств. Например, число и строку.
📌При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
в пару списков архивов 📌list-архивы также являются свойствами экземпляра
"""
import copy


class MyClass:
    lst = []

    def __init__(self, value, text):
        self.value = value
        self.text = text
        self.lst = copy.deepcopy(self.__class__.lst)
        self.__class__.lst.append(self)

    def __repr__(self):
        return f"Rectangle({self.value},{self.text})"


a = MyClass('1', 'a')
b = MyClass('2', 'b')
c = MyClass('3', 'c')

print(a.lst)
print(b.lst)
print(c.lst)
