# Записывает данные в файл.
def write_name(name):
    with open("telephone/telephone.txt","a", encoding="UTF-8") as file:
        file.write(name)

# Поиск данных в файле.
def search_data(char):
    with open("telephone/telephone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            if char in row:
                print(row)

# Замена данных в файле.
def change_file(old_line):
    with open("telephone/telephone.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        text = data.split("\n")
        change_text = text[old_line]
        id = input("Введите id: ")
        name = input("Введите ФИО: ")
        data = input("Введите дату рождения: ")
        tele = input("Введите номер телефона: ")
        res = id + ", " + name + ", " + data + ", " + tele
        text[old_line] = res
    with open("telephone/telephone.txt", "w", encoding="UTF-8") as file:
        file.write("\n".join(text))

 # Удаление строки в файле.
def delete_line(line_d):
    with open("telephone/telephone.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        text = data.split("\n")
        text.pop(line_d)
    with open("telephone/telephone.txt", "w", encoding="UTF-8") as file:
        file.write("\n".join(text))

# Сортировка данных.
def sorting_file(a):
    with open("telephone/telephone.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        lst.sort(key= lambda x: x.split(", ")[a-1])
    with open("telephone/telephone.txt", "w", encoding="UTF-8") as file:
        file.write("".join(lst))

# Вывод всех данных из файла.
def lst_output():
    with open("telephone/telephone.txt", "r", encoding="UTF-8") as file:
        print(file.read())