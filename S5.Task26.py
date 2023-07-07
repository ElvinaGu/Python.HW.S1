# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А 
# в целую степень B с помощью рекурсии.

# Ф-ция, которая возводит число в степень В
def power_num(n1, n2):
    if n2==0:
      return 1
    else:
       summa=n1
       if n2 != 1:
          summa = n1*power_num(n1, n2-1)
    return summa

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(power_num(a, b))