# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
# import random
#
# number = [1, 1, 2, 2, 3, 3]
# random.shuffle(number)
# print(number)
# for item in number:
#     if (count := number.count(item)) >= 2:
#         for _ in range(count//2):
#             number.remove(item)
#             number.remove(item)
# print(number)

user_input = input("Текст: ")
my_dict = {}

for item in user_input:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict)

for item in set(user_input):
    my_dict[item] = user_input.count(item)
print(my_dict)
