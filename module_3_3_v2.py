#Функция с параметрами по умолчанию:
def print_params(a, b, c):
    print(a, b, c)
print_params(1,'строка',True)

print_params(1,2) # не работает
print(print_params)

print_params(1,2,4, 5) # не работает
print(print_params)

print_params() # не работает
print(print_params)

print_params(b = 25, a = 1, c = True)
print(print_params)

#Распаковка параметров

values_list = [1,'строка',True]
print_params(*values_list)
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)
print(print_params)

#Распаковка + отдельные параметры

values_list_2 = [1,'строка']
print_params(*values_list_2, 42) # не работает
print(print_params)
