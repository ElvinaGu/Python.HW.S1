from database import *
from view import *

def main():
    while True:
        num = input_num()
        if num == 0:
            break
        if num == 1:
            res = input_name()
            write_name(res)
            print("Данные успешно записаны\n")
        if num == 2:
            char = input_char()
            search_data(char)
            print("Данные успешно найдены\n")
        if num == 3:
            lst_output()
            line = input_change()
            change_file(line)
            print("Данные успешно изменены\n")
        if num == 4:
            lst_output()
            line = input_delete()
            delete_line(line)
            print("Данные успешно удалены\n")
        if num == 5:
            sortin = char_sort()
            sorting_file(sortin)
            print("Данные успешно отсортированы\n")
        if num == 6:
            print("Полный список:")
            lst_output()

main()
