# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

word=str.upper(input("Введите слово: "))
text=list(word)
scores=0

for i in text:
    if i== 'А' or i== 'В' or i== 'Е' or i== 'И' or i== 'Н' or i== 'О' or i== 'Р' or i== 'С' or i== 'Т':
      scores += 1
    elif i == 'Д' or i == 'К' or i == 'Л' or i == 'М' or i == 'П' or i == 'У':
       scores +=2
    elif i == 'Б' or i == 'Г' or i == 'Ё' or i == 'Ь' or i == 'Я':
       scores +=3
    elif i == 'Й' or i == 'Ы':
       scores += 4
    elif i == 'Ж' or i == 'З' or i == 'Х' or i == 'Ц' or i == 'Ч':
       scores += 5
    elif i == 'Ш' or i == 'Э' or i == 'Ю':
       scores += 8
    elif i == 'Ф' or i == 'Щ' or i == 'Ъ':
       scores += 10

print(f"Полученные очки: {scores}")