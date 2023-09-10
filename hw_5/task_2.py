# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла

str_ = 'C:/Users/User/Desktop/Developer/FinalControl/linux.pdf'


def tuple_str(txt):
    *a, b = txt.split('/')
    return '/'.join(a), *b.split('.')


print(tuple_str(str_))
