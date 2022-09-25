def check_truth(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    answer = left == right
    return answer


print(check_truth(True, True, True))
print(check_truth(True, True, False))
print(check_truth(False, True, True))
print(check_truth(True, False, False))
print(check_truth(False, False, True))
print(check_truth(False, True, False))
print(check_truth(False, False, False))
print(check_truth(True, False, True))

print('Функция истина при всех значениях предикат')
