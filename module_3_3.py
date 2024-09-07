#Функция с параметрами по умолчанию:
def print_params(a, b, c):
    print(a, b, c)
print_params(1,'строка',True)

def print_params(a, b, c):
    print(a, b, c)
print_params(1,2) # не работает

def print_params(a, b, c):
    print(a, b, c)
print_params(1,2,4, 5) # не работает

def print_params(a, b, c):
    print(a, b, c)
print_params() # не работает

def print_params(a, b, c):
    print(a, b, c)
print_params(b = 25, a = 1, c = True)

#Распаковка параметров
def print_params(a, b, c):
    print(a, b, c)

values_list = [1,'строка',True]
print_params(*values_list)
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)

#Распаковка + отдельные параметры
def print_params(a, b):
    print(a, b)
values_list_2 = [1,'строка']
print_params(*values_list_2, 42) # не работает

