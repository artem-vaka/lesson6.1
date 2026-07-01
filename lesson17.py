import json
import os

FILENAME = "library.json"

def load_library():
    """Завантажує бібліотеку з файлу або створює нову."""
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("[Помилка] Файл пошкоджено. Створено нову порожню бібліотеку.")
        return {}
    except Exception as e:
        print(f"[Помилка при завантаженні]: {e}")
        return {}

def save_library(library):
    """Зберігає бібліотеку у JSON-файл."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(library, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[Помилка при збереженні]: {e}")

def add_book(library):
    """Додає нову книгу до бібліотеки."""
    print("\n--- Додавання книги ---")
    title = input("Назва книги: ").strip()
    author = input("Автор: ").strip()

    while True:
        try:
            year_input = input("Рік видання: ").strip()
            year = int(year_input)
            if year <= 0 or year > 2026:
                raise ValueError
            break
        except ValueError:
            print("[Помилка] Введіть коректний рік (число).")
            
    genre = input("Жанр: ").strip()

    if library:
        next_id = str(max(int(k) for k in library.keys()) + 1)
    else:
        next_id = "1"

    library[next_id] = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": False
    }
    
    save_library(library)
    print(f"Книгу «{title}» успішно додано з ID: {next_id}")

def print_book_info(book_id, info):
    """Допоміжна функція для красивого виведення книги."""
    status = " [Прочитано]" if info.get("read") else ""
    print(f"ID: {book_id}{status}")
    print(f"Назва: {info['title']}")
    print(f"Автор: {info['author']}")
    print(f"Рік видання: {info['year']}")
    print(f"Жанр: {info['genre']}\n")

def view_all_books(library):
    """Виводить список усіх книг та коротку статистику."""
    print("\n--- Перегляд усіх книг ---")
    if not library:
        print("Бібліотека порожня")
        return

    print(f"[Статистика] Усього книг у бібліотеці: {len(library)}\n")
    for book_id, info in library.items():
        print_book_info(book_id, info)

def delete_book(library):
    """Видаляє книгу за вказаним ID."""
    print("\n--- Видалення книги ---")
    if not library:
        print("Бібліотека порожня. Нічого видаляти.")
        return

    book_id = input("Введіть ID книги для видалення: ").strip()
    
    try:
        if book_id in library:
            removed_title = library[book_id]['title']
            del library[book_id]
            save_library(library)
            print(f"Книгу «{removed_title}» (ID: {book_id}) успішно видалено.")
        else:
            print("Книгу не знайдено")
    except Exception as e:
        print(f"[Помилка при видаленні]: {e}")

def find_books_by_author(library):
    """Шукає книги за іменем автора."""
    print("\n--- Пошук книг за автором ---")
    author_query = input("Введіть ім'я автора для пошуку: ").strip().lower()
    
    found = False
    for book_id, info in library.items():
        if author_query in info['author'].lower():
            print_book_info(book_id, info)
            found = True
            
    if not found:
        print("Книг цього автора не знайдено")

def find_books_by_genre(library):
    """Шукає книги за жанром."""
    print("\n--- Пошук книг за жанром ---")
    genre_query = input("Введіть жанр для пошуку: ").strip().lower()
    
    found = False
    for book_id, info in library.items():
        if genre_query in info['genre'].lower():
            print_book_info(book_id, info)
            found = True
            
    if not found:
        print("Книг цього жанру не знайдено")

def find_books_by_year(library):
    """Шукає книги за роком видання."""
    print("\n--- Пошук книг за роком видання ---")
    try:
        year_query = int(input("Введіть рік для пошуку: ").strip())
    except ValueError:
        print("[Помилка] Введіть коректне число (рік).")
        return
        
    found = False
    for book_id, info in library.items():
        if info['year'] == year_query:
            print_book_info(book_id, info)
            found = True
            
    if not found:
        print("Книг цього року не знайдено")

def mark_as_read(library):
    """Позначає книгу як прочитану."""
    print("\n--- Позначити книгу як прочитану ---")
    book_id = input("Введіть ID книги: ").strip()
    
    if book_id in library:
        library[book_id]["read"] = True
        save_library(library)
        print(f"Книгу «{library[book_id]['title']}» позначено як прочитану!")
    else:
        print("Книгу не знайдено")

def sort_books(library):
    """Сортує книги за обраним критерієм та напрямком (Від А до Я / Від Я до А)."""
    print("\n--- Сортування книг ---")
    if not library:
        print("Бібліотека порожня. Немає чого сортувати.")
        return

    print("1. Сортувати за назвою")
    print("2. Сортувати за автором")
    print("3. Сортувати за роком видання")
    print("4. Сортувати за жанром")
    
    sort_choice = input("Оберіть критерій сортування (1-4): ").strip()
    
    if sort_choice == "1":
        sort_key = lambda item: item[1]["title"].lower()
    elif sort_choice == "2":
        sort_key = lambda item: item[1]["author"].lower()
    elif sort_choice == "3":
        sort_key = lambda item: item[1]["year"]
    elif sort_choice == "4":
        sort_key = lambda item: item[1]["genre"].lower()
    else:
        print("[Помилка] Неправильний вибір критерію.")
        return


    print("\nОберіть напрямок сортування:")
    print("1. Від А до Я (або за зростанням для років)")
    print("2. Від Я до А (або за спаданням для років)")
    direction_choice = input("Ваш вибір (1-2): ").strip()

    if direction_choice == "1":
        is_reverse = False
    elif direction_choice == "2":
        is_reverse = True
    else:
        print("[Помилка] Неправильний вибір напрямку.")
        return

    sorted_library = sorted(library.items(), key=sort_key, reverse=is_reverse)

    print("\n--- Результат сортування ---")
    for book_id, info in sorted_library:
        print_book_info(book_id, info)

def main():
    """Головний цикл програми."""
    library = load_library()
    
    while True:
        print("\n--- Бібліотека книг ---")
        print("1. Додати книгу")
        print("2. Переглянути всі книги")
        print("3. Видалити книгу")
        print("4. Знайти книгу за автором")
        print("5. Знайти книгу за жанром")
        print("6. Знайти книгу за роком видання")
        print("7. Позначити книгу як прочитану")
        print("8. Сортувати книги")
        print("9. Вийти")
        
        choice = input("Виберіть пункт меню (1-9): ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_all_books(library)
        elif choice == "3":
            delete_book(library)
        elif choice == "4":
            find_books_by_author(library)
        elif choice == "5":
            find_books_by_genre(library)
        elif choice == "6":
            find_books_by_year(library)
        elif choice == "7":
            mark_as_read(library)
        elif choice == "8":
            sort_books(library)
        elif choice == "9":
            print("Дякуємо за використання програми. Бувай!")
            break
        else:
            print("[Помилка] Неправильний вибір. Спробуйте ще раз (1-9).")

if __name__ == "__main__":
    main()
