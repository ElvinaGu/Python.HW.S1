# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n=int(input("Введите кол-во эл-ов в массиве: "))
a=[i for i in range(1,n+1)]
print(*a)

num=int(input("Введите число: "))
count=0
for i in a:
    if i==num:
        count += 1
print(f"Элемент повторяется {count} раз(а)")

