n = int(input('Введите значение длины списка и затем сам список: '))
a = []

for i in range(n):
    a.append(int(input()))

print('Исходный писок:')
print(a)
k = 0

for i in range(n - 1):
    for j in range(n - 1):
        k += 1
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print('Отсортированный список:')
print(a)

print('Количество операций = ', k)