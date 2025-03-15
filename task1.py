from typing import Tuple

def total_salary(path: str) -> Tuple[int, float]:
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    _, salary = line.rsplit(",", 1) 
                    total += int(salary.strip()) 
                    count += 1
                except ValueError:
                    print(f"Помилка: некоректний формат рядка: {line.strip()}")

        if count == 0:
            return (0, 0.0)  # Avoiding devision by zero

        return total, total / count

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

    return (0, 0.0)

print(total_salary('salary_file.txt'))