# 1 камень числа 3-20
# 2 камень - без чисел
# пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.

def password(p):
    result = ""
    for i in range(1, p):
        for j in range(i+1, p+1):
            if p % (i + j) == 0:
                result += str(i) + str(j)
    return result

p = int(input('Введите число от 3 до 20: '))
result = password(p)
print('Пароль: ', result)


