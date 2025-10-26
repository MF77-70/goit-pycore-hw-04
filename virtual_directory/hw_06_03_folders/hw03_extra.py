"""
_extra = Заменили обычные пробельные отступы на символы псевдографики (├──, │, └──),
визуализировать дерево директорий — теперь структура отображается не просто списком, а в виде
иерархии с ветками, как в файловом менеджере
"""

import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація кольорів
init(autoreset=True)

# Кольори для елементів
DIR_COLOR = Fore.BLUE
FILE_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
INFO_COLOR = Fore.CYAN
LINE_COLOR = Fore.LIGHTBLACK_EX # ← колір для ліній (білий)

# Символи для побудови дерева
BRANCH = "├── "
LAST_BRANCH = "└── "
VERTICAL = "│   "
EMPTY = "    "

def visualize_directory_tree(path: Path, prefix: str = ""):
    """
    Виводить структуру директорії у форматі дерева (як у команді tree),
    з білими лініями ├── │ └──.
    """
    try:
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        print(f"{prefix}{ERROR_COLOR}⚠️  Немає доступу до: {path.name}")
        return

    for i, item in enumerate(items):
        connector = LAST_BRANCH if i == len(items) - 1 else BRANCH

        # Формуємо префікс: білі лінії + кольоровий елемент
        branch_part = f"{LINE_COLOR}{connector}{Style.RESET_ALL}"

        if item.is_dir():
            print(f"{prefix}{branch_part}{DIR_COLOR}📁 {item.name}{Style.RESET_ALL}")
            extension = EMPTY if i == len(items) - 1 else VERTICAL
            visualize_directory_tree(item, prefix + LINE_COLOR + extension + Style.RESET_ALL)
        else:
            print(f"{prefix}{branch_part}{FILE_COLOR}📄 {item.name}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{ERROR_COLOR}Використання: python {sys.argv[0]} <шлях_до_директорії>")
        sys.exit(1)

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"{ERROR_COLOR}Помилка: шлях '{target}' не існує.")
        sys.exit(1)

    if not target.is_dir():
        print(f"{ERROR_COLOR}Помилка: шлях '{target}' не є директорією.")
        sys.exit(1)

    print(f"{INFO_COLOR}Структура директорії: {target.resolve()}{Style.RESET_ALL}")
    visualize_directory_tree(target)
