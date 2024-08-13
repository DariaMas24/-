immutable_var = 1, 'cat'
print(immutable_var)
print(type(immutable_var))
mutable_list = ([3, 4], 5, 6)
print(mutable_list)
mutable_list[0][1] = 2
print(mutable_list)


immutable_var [1] = 'dog' # кортеж не поддерживает обращение по элементам