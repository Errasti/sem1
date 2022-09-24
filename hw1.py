day = int(input('Введите номер дня недели: '))
if 1 <= day <= 5:
    print("нет")
elif day == 6 or day == 7:
    print('да')
else:
    print("Некорректное значение. Введите от 1 до 7")
