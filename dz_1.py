# задача 1
import random
nachalo = int(input('Введите начальное число списка: '))
shag = int(input('Шаг: '))
elements = int(input('Кол-во элементов: '))

print(nachalo, shag, elements)

for i in range(elements):
    print(nachalo+i*shag)


# задача 2

a = [random.randint(-10, 20) for _ in range(20)]
print(a)
my_min = 7
my_max = 12

for i in range(len(a)):
    if my_min <= a[i] <= my_max:
        print(a[i])
