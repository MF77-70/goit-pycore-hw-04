from colorama import Fore, Style, init

init(autoreset=True)

def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та її аргументи.
    Команда перетворюється у нижній регістр.
    """
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


# --- тут функции команд ---

def add_contact(args, contacts):
    """
    Додає новий контакт до словника contacts.
    Очікує 2 аргументи: ім’я та номер телефону.
    """
    if len(args) != 2:
        return Fore.RED + "Неправильна кількість аргументів для команди 'add'. Очікується: [ім’я] [номер телефону]." + Style.RESET_ALL
    name, phone = args 
    contacts[name] = phone
    return Fore.GREEN + "Контакт додано." + Style.RESET_ALL


def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту у словнику contacts.
    Очікує 2 аргументи: ім’я та новий номер телефону.
    """
    if len(args) != 2:
        return  Fore.RED + "Неправильна кількість аргументів для команди 'change'. Очікується: [ім’я] [новий номер телефону]."  + Style.RESET_ALL

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return Fore.GREEN + "Контакт оновлено." + Style.RESET_ALL
    else:
        return Fore.RED + "Контакт не знайдено." + Style.RESET_ALL


def show_phone(args, contacts):
    """
    Показує номер телефону для вказаного контакту.
    Очікує 1 аргумент: ім’я.
    """
    if len(args) != 1:
        return Fore.RED + "Неправильна кількість аргументів для команди 'phone'. Очікується: [ім’я]." + Style.RESET_ALL
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return Fore.RED + "Контакт не знайдено." + Style.RESET_ALL


def show_all(contacts):
    """
    Показує всі збережені контакти та їхні номери телефонів.
    Не очікує аргументів.
    """
    if not contacts:
        return Fore.RED + "Немає збережених контактів." + Style.RESET_ALL
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


# --- тут основна функція програми ---

def main():
    """
    Основна функція бота, що керує циклом обробки команд.
    """
    contacts = {}
    print(Fore.CYAN + "Вітаю у помічнику-боті!"+ Style.RESET_ALL)

    while True:
        user_input = input(Fore.YELLOW + "Введіть команду: " + Style.RESET_ALL)

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.CYAN + "До побачення!" + Style.RESET_ALL)
            break
        elif command == "hello":
            print(Fore.CYAN + "Чим можу допомогти?" + Style.RESET_ALL)
        elif command == "add":
            print(add_contact(args, contacts))  # Викликаємо add_contact
        elif command == "change":
            print(change_contact(args, contacts))  # Викликаємо change_contact
        elif command == "phone":
            print(show_phone(args, contacts))  # Викликаємо show_phone
        elif command == "all":
            print(show_all(contacts))  # Викликаємо show_all
        else:
            print(Fore.RED + "Невідома команда." + Style.RESET_ALL)


if __name__ == "__main__":
    # Этот блок гарантирует, что функция main() будет вызвана только тогда,
    # когда скрипт запускается напрямую, а не импортируется как модуль.
    main()