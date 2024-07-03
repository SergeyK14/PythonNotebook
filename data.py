from datetime import date, datetime, time


def text_note():
    note = input("Введите текст заметки: ")
    return note


def input_date():
    note_date = [datetime.now().date().day, datetime.now().date().month, datetime.now().date().year]
    note_time = [datetime.now().time().hour, datetime.now().time().minute]
    for i in range(len(note_date)):
        if note_date[i] < 10:
            note_date[i] = str(f'0{note_date[i]}')
    for i in range(len(note_time)):
        if note_time[i] < 10:
            note_time[i] = str(f'0{note_time[i]}')
    note_date = list(map(str, note_date))
    note_time = list(map(str, note_time))
    return '.'.join(note_date), ':'.join(note_time)


def input_themes():
    themes = input("Введите тему заметки: ")
    return themes


def note_id():
    note_id = [datetime.now().date().year, datetime.now().date().month, datetime.now().date().day, datetime.now().time().hour, datetime.now().time().minute, datetime.now().time().second]
    for i in range(len(note_id)):
        if note_id[i] < 10:
            note_id[i] = str(f'0{note_id[i]}')
    note_id = list(map(str, note_id))
    return ''.join(note_id)
