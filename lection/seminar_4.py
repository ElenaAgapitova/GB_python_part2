# my_dict = {'a': 3, 'b': 7, 'c': 1}
# print(sorted(my_dict.items()))
# print(sorted(my_dict.items(), key=lambda x: x[1]))

# data = [25, -42, 146, 73, -100, 12]
# print(list(map(str, data)))
# print(max(data, key=lambda x: -x))
# print(*filter(lambda x: not x[0].startswith('__'), globals().items()))

a = (1, 2, [4, 5])
b = a
a[2][0] = 5
b[2][0] = 4
print(a)
print(b)
