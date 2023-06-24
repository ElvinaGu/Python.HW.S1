# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые 
# нужно перевернуть

from random import randint
n=int(input("Введите кол-во монеток: "))

orel=0
reshka=0

for i in range(n):
  side=randint(0,1)
  print(side, end=" ")
  if side == 0:
    orel +=1
  else:
    reshka +=1

if reshka>orel:
  print(f"\n{orel} монет необходимо перевернуть")
else:
  print(f"\n{reshka} монет необходимо перевернуть")