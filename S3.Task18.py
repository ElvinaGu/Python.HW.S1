# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n=int(input("Введите кол-во эл-ов в массиве: "))
a=[i for i in range(1,n+1)]
print(*a)

num=int(input("Введите число: "))
x=a[0]
for i in a:
    if abs(i-num) < abs(x-num):
        x=i
print(f"Самый близкий по величине элемент: {x}")   