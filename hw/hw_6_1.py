def total_salary(path):
    salaries = {}  # створюємо порожній словник, де будемо зберігати імена зарплати

    try:
        with open(path, 'r', encoding='utf-8') as file:

            for line in file: # проходимо по кожному рядку у файлі
                cleaned_line = line.strip() # видаляємо пробіли
                if not line: # пропускаємо порожній рядок
                    continue
                
                name, salary = cleaned_line.split(',') # розділяємо рядок на дві частини - ім'я та зарплату 
                salaries[name] = int(salary)  # додаємо до словника перетворюючи зарплати в integer

        
        total = sum(salaries.values()) # роозраховуємо загальну та середню суму зарплат
        average = total / len(salaries) 

        return total, average, salaries

    except FileNotFoundError: # якщо файл не знайдено або інша помилка — повертаємо нулі замість помилки
        print("Файл відсутній")
        return 0, 0
    except Exception:
        print("Виникла помилка під час обробки файлу.")
    return 0, 0


# Перевірка
total, average, salaries = total_salary('salary_file.txt')

print(f"Загальна сума заробітної плати: {total}, Середня: {average}")

print(salaries)
print (total, average, salaries)

