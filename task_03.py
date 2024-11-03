import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def display_directory_structure(path, level=0):
    try:
        path_obj = Path(path)
        if not path_obj.exists():
            print(Fore.RED + "Шлях не існує.")
            return
        if not path_obj.is_dir():
            print(Fore.RED + "Вказаний шлях не є директорією.")
            return

        # Рекурсивний обхід директорії
        for item in path_obj.iterdir():
            indent = " " * 4 * level
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                # Рекурсивний виклик для вкладених папок
                display_directory_structure(item, level + 1)
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")

    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
    else:
        directory_path = sys.argv[1]
        display_directory_structure(directory_path)
