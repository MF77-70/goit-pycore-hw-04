def get_cats_info(path):
    cats_info = []

    try:
        with open (path, 'r', encoding='utf-8') as file:
            for line in file:                
                cleaned_line = line.strip() # 
                splitted_parts = cleaned_line.split(',')

                if len(splitted_parts) == 3:

                    cat_id, cat_name, cat_age = splitted_parts

                    cat_dict = {
                    'id': cat_id,
                    'name' : cat_name,
                    'age' : cat_age 
               }              
                cats_info.append(cat_dict)                

            else:
                print(f'Увага! Некоректний формат: {cleaned_line}')          

    except FileNotFoundError: 
        print('Файл відсутній')
        return [] # якщо файл не знайдено або інша помилка - повертаємо порожній список
    except Exception as e:
        print('Виникла помилка під час обробки файлу:', e)
        return []

    return cats_info

# Перевірка

cats_info = get_cats_info('cats_file.txt')
print(cats_info)


non_existent_cats_info = get_cats_info('non_existent_file.txt')

    
