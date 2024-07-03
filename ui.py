from logger import input_note, print_notes, edit_note, del_note, filter_text_input, filtered_list_creation, all_notes_list


def interface():
    print("""Программа для работы с заметками. 
    Основное меню. Выберите параметр для работы с заметками:
        1 - запись заметки,
        2 - вывод заметок, 
        3 - поиск заметок по параметрам,
        0 - завершение работы программы.
        """)
    command_number = int(input("Введите номер команды: "))
    while command_number < 0 or command_number > 5:
        command_number = int(input("Введите корректный номер команды: "))
    return command_number


def del_edit_ui():
    print("""Программа для работы с заметками. 
    Подменю редактирования. Выберите параметр для работы с заметками:
            1 - редактирование заметки,
            2 - удаление заметки,
            0 - выход в основное меню.
            """)
    try:
        edit_command_number = int(input("Введите номер команды: "))
        while edit_command_number < 0 or edit_command_number > 2:
            edit_command_number = int(input("Введите корректный номер команды: "))
        return edit_command_number
    except ValueError:
        edit_command_number = int(input("Введите числовое значение: "))
        return edit_command_number


def del_edit_submenu(notelist):
    notelist_to_edit = notelist
    command_number = del_edit_ui()
    for i in range(100):
        if command_number == 0:
            break
            return False
        else:
            note_number = int(input("Введите номер заметки из списка: "))
            if note_number > len(notelist_to_edit) - 1:
                print("Введен некорректный номер заметки")
                continue
            else:
                if command_number == 1:
                    new_note_text = input("Введите новый текст заметки: ")
                    edit_note(notelist_to_edit, note_number, new_note_text)
                elif command_number == 2:
                    del_note(notelist_to_edit, note_number)
                choice = input("Продолжить редактирование (Y/N): ")
                if choice.lower() == 'y':
                    del_edit_ui()
                else:
                    break


def main_menu():
    command_number = interface()
    while command_number != 0:
        if command_number == 1:
            input_note()
        elif command_number == 2:
            notelist_to_print = all_notes_list()
            print("Вывод всех ваших заметок: ")
            print_notes(notelist_to_print)
            del_edit_submenu(notelist_to_print)
        elif command_number == 3:
            print('Введите параметры поиска через ";": ')
            notelist_to_sort = filtered_list_creation()
            print_notes(notelist_to_sort)
            del_edit_submenu(notelist_to_sort)
        choice = input("Продолжить работу с программой?: Y/N  ")
        if choice.lower() == "y":
            command_number = interface()
        else:
            break
