def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Видаляємо зайві пробіли з рядка та розділяємо за комами
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats.append(cat_info)
                else:
                    print(f"Некоректний формат рядка: {line.strip()}")
        return cats
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

# Приклад використання функції
cats_info = get_cats_info("C:/Users/Xiaomi/Documents/@ DEV/GoIT/Homework/goit-pycore-hw-04/cats_file.txt")
print(cats_info)
