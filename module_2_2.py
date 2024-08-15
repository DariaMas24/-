first = input('ВВЕДИТЕ ПЕРВОЕ ЦЕЛОЕ ЧИСЛО: ')
second = input('ВВЕДИТЕ ВТОРОЕ ЦЕЛОЕ ЧИСЛО: ')
third = input('ВВЕДИТЕ ТРЕТЬЕ ЦЕЛОЕ ЧИСЛО: ')
if first == second == third:
        print(3)
if first == second or first == third or second == third:
        print(2)
if first != second or first != third or second != third:
    print(0)