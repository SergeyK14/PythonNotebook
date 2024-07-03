import os
from data import text_note, input_date, input_themes, note_id
from itertools import groupby

file_name = "notes.csv"


def filter_text_input():
    filter_text = input()
    return filter_text


def file_path_check():
    if os.path.exists(file_name):
        return True
    else:
        with open(file_name, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines('ID;Дата;Время;Тема;Текст\n')
        return False


def file_rewrite(list_to_rewrite: list):
    if file_path_check():
        with open(file_name, 'w', encoding='utf-8', newline='\n') as f:
            f.write(''.join(list_to_rewrite))
    else:
        print("Заметок нет, файл создан.")

def all_notes_list():
    if file_path_check():
        with open(file_name, 'r', encoding="utf-8", newline='\n') as file:
            list_data = [i for i in file.readlines()]
            return list_data
    else:
        print("Заметок нет, файл создан.")

def print_notes(notelist_to_print: list):
    if file_path_check() is True:
        try:
            if not notelist_to_print[1:]:
                print("***Заметок нет***")
            else:
                print('№. ' + notelist_to_print[0].replace('\n', ''))
                for i, element in enumerate(notelist_to_print[1:]):
                    element = element.replace('\n', '')
                    print(f"{i+1}. {element}")
        except TypeError:
            print("***Заметок нет***")
    else:
        print("Заметок нет, файл создан")


def input_note():
    if file_path_check():
        print("Введите вашу заметку для записи в файл: ")
        theme = input_themes()
        note = text_note()
        note_date = input_date()
        n_id = note_id()
        with open(file_name, 'a', encoding="utf-8", newline='\n') as file:
            file.writelines(f"{n_id};{note_date[0]};{note_date[1]};{theme};{note}\n")
    else:
        print("Заметок нет, файл создан.")


def filtered_list_creation():
    if file_path_check():
        filter_string = filter_text_input()
        list_data = all_notes_list()
        filtered_list = []
        filtered_list.append(list_data[0])
        if ";" in filter_string:
            list_filter = filter_string.split(';')
        else:
            list_filter = [filter_string]
        for element in list_data[1:]:
            temp_record = element.split(';')
            for record in temp_record:
                for element_filter in list_filter:
                    if element_filter.lower() in record.lower():
                        filtered_list.append(element)
        return [el for el, _ in groupby(filtered_list)]
    else:
        print("Заметок нет, файл создан.")


def edit_note(notelist, note_number, new_note_text):
    if file_path_check():
        all_notes_listing = all_notes_list()
        for i, note in enumerate(notelist):
            if note_number == i:
                note_to_edit = note.split(';')
                break
        edit_note_id = note_to_edit[0]
        for j, element in enumerate(all_notes_listing):
            if j == 0:
                continue
            else:
                element_id = element[0:14]
            if element_id == edit_note_id:
                element_to_edit = element.split(';')[0:5]
                element_to_edit[4] = f'{new_note_text}\n'
                all_notes_listing[j] = ';'.join(element_to_edit[0:5])
        file_rewrite(all_notes_listing)
    print("Заметок нет, файл создан.")


def del_note(notelist, note_number):
    if file_path_check():
        all_notes_listing = all_notes_list()
        for i, note in enumerate(notelist):
            if note_number == i:
                note_to_delete = note.split(';')
                break
        del_note_id = note_to_delete[0]
        for j, element in enumerate(all_notes_listing):
            if j == 0:
                continue
            else:
                element_id = element[0:14]
            if element_id == del_note_id:
                option = input("Вы желаете удалить заметку? Y/N: ")
                if option.lower() == "y":
                    all_notes_listing.pop(j)
                else:
                    print("***Операция отменена***")
        file_rewrite(all_notes_listing)
    else:
        print("Заметок нет, файл создан.")