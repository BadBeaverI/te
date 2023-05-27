phone_book = {}
def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data

def printinfo(data):
    for i in data:
        print('выберите пункт меню', i)

data = readfile('tel.txt')

def add_contact(name, number):
    phone_book[name] = number
    print(f"Контакт {name} добавлен в справочник.")

def search_contact(name):
    if name in phone_book:
        number = phone_book[name]
        print(f"Номер телефона {name}: {number}")
    else:
        print(f"Контакт {name} не найден в справочнике.")

def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} удален из справочника.")
    else:
        print(f"Контакт {name} не найден в справочнике.")

def update_contact(name):
    if name in phone_book:
        new_number = input(f"Введите новый номер телефона для контакта {name}: ")
        phone_book[name] = new_number
        print(f"Номер телефона для контакта {name} обновлен.")
    else:
        print(f"Контакт {name} не найден в справочнике.")

def view_phone_book():
    try:
        with open("tel.txt", "r") as file:
            print("Телефонный справочник:")
            for line in file:
                line = line.strip()
                if line:
                    name, number = line.split(":")
                    print(f"{name}: {number}")
                else:
                    print("Ошибка: некорректная строка в файле справочника.")
    except FileNotFoundError:
        print("Файл справочника не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def main_menu():
    while True:
        print("Телефонный справочник")
        print("1. Добавить контакт")
        print("2. Найти контакт по имени")
        print("3. Удалить контакт")
        print("4. Изменить контакт")
        print("5. Просмотреть весь справочник")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            number = input("Введите номер телефона: ")
            add_contact(name, number)
        elif choice == "2":
            name = input("Введите имя контакта: ")
            search_contact(name)
        elif choice == "3":
            name = input("Введите имя контакта для удаления: ")
            delete_contact(name)
        elif choice == "4":
            name = input("Введите имя контакта для изменения: ")
            update_contact(name)
        elif choice == "5":
            view_phone_book()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Запуск главного меню
main_menu()
