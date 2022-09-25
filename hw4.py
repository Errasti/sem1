quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('x > 0 и y > 0')
elif quarter == 2:
    print('x < 0 и y > 0')
elif quarter == 3:
    print('x < 0 и y < 0')
elif quarter == 4:
    print('x > 0 и y < 0')
else:
    print('Некорректный ввод данных. Введите от 1 до 4 цифрой')
