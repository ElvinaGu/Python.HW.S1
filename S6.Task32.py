# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

lst = [random.randint(-10,30) for i in range(10)]
print(lst)

mini_diapazon = int(input("Введите необходимый диапазон. Минимальное значение: "))
maxi_diapazon = int(input("Введите необходимый диапазон. Максимальное значение: "))

lst2 = []
for i in range(len(lst)):
    if mini_diapazon <= lst[i] <= maxi_diapazon:
        lst2.append(i)

print(*lst2)