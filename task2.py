from typing import List, Dict

def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                parts = line.strip().split(',')

                if len(parts) != 3:
                    print(f"Помилка: некоректний формат рядка: {line_number}: {line.strip()}")
                    continue 

                id_, name, age = parts

                if not age.isdigit():
                    print(f"Помилка: некоректний вік у рядку {line_number}: {line.strip()}")
                    continue

                cats_info.append({"id": id_, "name": name, "age": age})

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

    return cats_info

print(get_cats_info("cats_file.txt"))
