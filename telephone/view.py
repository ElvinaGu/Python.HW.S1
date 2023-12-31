# Выбор действий для работы с файлом.
def input_num():
    ask = int(input("Выберите дейстие:\n1 - Записать нового пользователя;\n2 - Поиск по характеристике;"
                    "\n3 - Изменить данные пользователя;\n4 - Удалить данные пользователя;\n"
                    "5 - Отсортировать список;\n6 - Вывести весь список пользователей;\n0 - Выход из программы.\n"))
    return ask

# Внесение данных в файл.
def input_name():
    id = input("Введите id: ")
    name = input("Введите ФИО: ")
    data = input("Введите дату рождения: ")
    tele = input("Введите номер телефона: ")
    res = id + ", " + name + ", " + data + ", " + tele + "\n"
    return res

# Данные для поиска.
def input_char():
    char = input("Введите характеристику поиска: ")
    return char

# Информация по замене данных.
def input_change():
    change = int(input("Какую строку Вы хотите изменить: ")) - 1
    return change

# Удаление строки.
def input_delete():
    delete = int(input("Какую строку Вы хотите удалить: ")) - 1
    return delete

# Ввод данных по сортировке.
def char_sort():
    ask = int(input("Отсортировать по:\n1 - id;\n2 - ФИО\n"))
    return ask