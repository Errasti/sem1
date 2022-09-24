a = int(input('Введите число: '))
result = []

for i in range(2, a):
    while a % i == 0:
        result.append(i)
        a = a // i

print(result)
