def import_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contacts.append({
                    'last_name': data[0],
                    'first_name': data[1],
                    'middle_name': data[2],
                    'phone_number': data[3]
                })
        print("Контакты успешно импортированы.")
    except FileNotFoundError:
        print("Файл не найден.")
    return contacts


def export_contacts(filename, contacts):
    try:
        with open(filename, 'w') as file:
            for contact in contacts:
                file.write(f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']}\n")
        print("Контакты успешно экспортированы.")
    except:
        print("Ошибка при экспорте контактов.")


def search_contact(contacts, key, value):
    result = []
    for contact in contacts:
        if contact[key] == value:
            result.append(contact)
    return result


def print_contacts(contacts):
    if contacts:
        for contact in contacts:
            print(f"{contact['last_name']} {contact['first_name']} {contact['middle_name']}: {contact['phone_number']}")
    else:
        print("Контакт не найден.")


def add_contact(contacts):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contacts.append({
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    })
    print("Контакт успешно добавлен.")


def copy_contact(filename_from, filename_to, index):
    try:
        with open(filename_from, 'r') as file_from:
            data = file_from.readlines()
            with open(filename_to, 'a') as file_to:
                file_to.write(data[index])
        print("Контакт успешно скопирован.")
    except FileNotFoundError:
        print("Файл не найден.")
    except IndexError:
        print("Неверный номер строки.")


def main():
    filename = "contacts.txt"
    contacts = import_contacts(filename)

    while True:
        print("\nМеню:")
        print("1. Вывести все контакты")
        print("2. Найти контакт")
        print("3. Добавить контакт")
        print("4. Скопировать контакт из файла")
        print("5. Экспортировать контакты")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            print_contacts(contacts)
        elif choice == '2':
            key = input("Введите характеристику для поиска (например, имя или фамилию): ")
            value = input("Введите значение: ")
            found_contacts = search_contact(contacts, key, value)
            print_contacts(found_contacts)
        elif choice == '3':
            add_contact(contacts)
        elif choice == '4':
            filename_from = input("Введите имя файла, откуда копировать: ")
            index = int(input("Введите номер строки, которую нужно скопировать: "))
            copy_contact(filename_from, filename, index)
        elif choice == '5':
            export_contacts(filename, contacts)
        elif choice == '6':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()