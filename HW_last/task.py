import json
import datetime

FILE_PATH = "defter.json"

def load_notes():
    try:
        with open(FILE_PATH, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(FILE_PATH, "w") as file:
        json.dump(notes, file, indent=4)

def list_notes(notes):
    if not notes:
        print("Заметок нет.")
        return

    for note in notes:
        print(note)

def add_note():
    title = input("Заголовок заметки: ")
    body = input("Текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)

def edit_note():
    note_id = int(input("ID заметки: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Новый заголовок: ")
            note["body"] = input("Новый текст: ")
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break

def delete_note():
    note_id = int(input("ID заметки: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            break

notes = load_notes()

while True:
    print("1. Добавить заметку")
    print("2. Сохранить заметки")
    print("3. Вывести список заметок")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("6. Выйти")
    print()

    choice = input("Выберите действие: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        save_notes(notes)
    elif choice == "3":
        list_notes(notes)
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        break

    print()