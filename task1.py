import os
import shutil
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

def copy_files_by_extension(src_dir, dest_dir="dist"):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                copy_files_by_extension(item_path, dest_dir)
            elif os.path.isfile(item_path):
                ext = os.path.splitext(item)[1][1:] or "no_extension"
                ext_dir = os.path.join(dest_dir, ext)

                os.makedirs(ext_dir, exist_ok=True)
                shutil.copy2(item_path, ext_dir)
                print(Fore.GREEN + f"✅ Скопійовано: {item_path} → {ext_dir}")
    except Exception as e:
        print(Fore.RED + f"❌ Помилка: {e}")

def main():
    parser = argparse.ArgumentParser(description="Копіює файли за розширенням у відповідні підтеки.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    
    args = parser.parse_args()

    if not os.path.exists(args.source):
        print(Fore.RED + "❌ Вихідна директорія не існує.")
        return

    os.makedirs(args.destination, exist_ok=True)
    print(Fore.CYAN + f"📁 Починаємо копіювання з {args.source} до {args.destination}")
    copy_files_by_extension(args.source, args.destination)
    print(Fore.BLUE + Style.BRIGHT + "🎉 Готово! Файли розсортовано.")

if __name__ == "__main__":
    main()

