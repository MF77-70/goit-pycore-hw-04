import sys

def total_salary(path):
    salaries = {}
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                name, salary = cleaned_line.split(',')
                salaries[name] = int(salary)

        total = sum(salaries.values())
        average = total / len(salaries)
        return total, average, salaries

    except FileNotFoundError:
        print("Файл відсутній.")
        return 0, 0, {}
    except Exception:
        print("Виникла помилка під час обробки файлу.")
        return 0, 0, {}

# --- точка входу програми ---
if __name__ == "__main__":
    # Перевіряємо, чи передано шлях до файлу
    if len(sys.argv) < 2:
        print("Використання: python total_salary.py <шлях_до_файлу>")
        sys.exit(1)

    # Отримуємо шлях із аргументів
    path = sys.argv[1]

    # Викликаємо функцію з цим шляхом
    total, average, salaries = total_salary(path)

    # Виводимо результати
    print(f"Загальна сума зарплат: {total}")
    print(f"Середня зарплата: {average}")
    print(f"Деталі: {salaries}")
