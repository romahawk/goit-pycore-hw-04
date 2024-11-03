def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            print("Файл відкрито успішно. Зміст файлу:")
            for line in file:
                print(f"Рядок з файлу: '{line.strip()}'")  # Перевірка рядка
                
                # Розбивання на ім'я та зарплату
                try:
                    name, salary = line.strip().split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка в рядку: '{line.strip()}'")  # Діагностика проблемних рядків
                    continue  # Пропуск рядків з помилкою формату

        average = total / count if count > 0 else 0
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0

# Запуск функції для перевірки
total, average = total_salary("c:/Users/Xiaomi/Documents/@ DEV/GoIT/Homework/goit-pycore-hw-04/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
