import sys
from pathlib import Path
from colorama import Fore, Style, init

# після кожного print колір автоматично повертається до стандартного.
init(autoreset=True)

# Визначаємо кольори для різних типів елементів.
DIR_COLOR = Fore.BLUE
FILE_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
INFO_COLOR = Fore.CYAN
WARNING_COLOR = Fore.YELLOW


def visualize_directory_structure(directory_path: Path, indent_level: int = 0):
    """
       Аргументи:
        directory_path (Path): шлях до поточної директорії (об’єкт Path).
        indent_level (int): рівень вкладеності для формування відступів у виведенні.
                            За замовчуванням 0 — для кореневої директорії.
    """
    # Формуємо відступ: кожен рівень додає 4 пробіли.
    indent = "    " * indent_level

    try:
        # Проходимо всі елементи у поточній директорії (папки та файли).
        for item in directory_path.iterdir():
            if item.is_dir():
                # Якщо елемент — це директорія (папка):
                # Виводимо її ім’я синім кольором і рекурсивно заходимо всередину.
                print(f"{indent}{DIR_COLOR}📂 {item.name}")
                visualize_directory_structure(item, indent_level + 1)
            elif item.is_file():
                # Якщо елемент — це файл: виводимо його ім’я зеленим кольором.
                print(f"{indent}{FILE_COLOR}📄 {item.name}")
            
    except PermissionError:
        # Якщо немає прав доступу до директорії — повідомляємо користувача.
        print(f"{indent}{WARNING_COLOR}⚠️ Немає доступу до директорії: {directory_path.name}")
    except Exception as e:
        # Загальна обробка будь-яких інших неочікуваних помилок.
        print(f"{indent}{ERROR_COLOR}❌ Помилка під час обходу '{directory_path.name}': {e}")


if __name__ == "__main__":
    # Цей блок виконується лише тоді, коли скрипт запускають напряму, а не імпортують як модуль у іншу програму.

    # Перевіряємо, що користувач передав рівно один аргумент — шлях до директорії.
    if len(sys.argv) != 2:
        print(f"{ERROR_COLOR}Використання: python {sys.argv[0]} <шлях_до_директорії>")
        sys.exit(1)  # Завершуємо програму з кодом помилки 1.

    # Отримуємо шлях, який передано користувачем.
    target_path_str = sys.argv[1]
    # Створюємо об’єкт Path для зручної роботи з файловою системою.
    target_path = Path(target_path_str)

    # Перевіряємо, чи існує такий шлях.
    if not target_path.exists():
        print(f"{ERROR_COLOR}Помилка: шлях '{target_path_str}' не існує.")
        sys.exit(1)

    # Перевіряємо, чи є цей шлях саме директорією (а не файлом).
    if not target_path.is_dir():
        print(f"{ERROR_COLOR}Помилка: шлях '{target_path_str}' не є директорією.")
        sys.exit(1)

    # Якщо всі перевірки пройдені — виводимо заголовок і починаємо візуалізацію.
    print(f"{INFO_COLOR}Структура директорії: {target_path_str}")
    visualize_directory_structure(target_path)


# Перевірки
''''
python hw03.py
python hw03.py non_existent_folder
python hw03.py hw03.py
python hw03.py .
'''


