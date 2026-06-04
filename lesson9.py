import json
from datetime import datetime

PLANNER_FILE = 'planner.json'


def load_events():
    try:
        with open(PLANNER_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            print('[!] Помилка: невірний формат файлу, створюється порожній планувальник')
            return {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print('[!] Помилка: файл містить пошкоджені дані, створюється порожній планувальник')
        return {}
    except Exception as e:
        print(f'[!] Помилка при відкритті файлу: {e}')
        return {}


def save_events(events):
    try:
        with open(PLANNER_FILE, 'w', encoding='utf-8') as file:
            json.dump(events, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'[!] Помилка при збереженні файлу: {e}')


def get_next_id(events):
    try:
        if not events:
            return '1'
        return str(max(int(event_id) for event_id in events.keys()) + 1)
    except Exception:
        return str(len(events) + 1)


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print('[!] Помилка! Значення не може бути пустим')


def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_time(time_text):
    try:
        datetime.strptime(time_text, '%H:%M')
        return True
    except ValueError:
        return False


def parse_event_datetime(event):
    try:
        return datetime.strptime(f"{event.get('date', '')} {event.get('time', '')}", '%Y-%m-%d %H:%M')
    except Exception:
        return datetime.max


def sort_by_event_id(event_id):
    try:
        return int(event_id)
    except ValueError:
        return 0


def format_status(event):
    return 'Виконано' if event.get('completed', False) else 'Не виконано'


def add_event(events):
    title = read_non_empty('Назва події: ')

    while True:
        date_text = read_non_empty('Дата (YYYY-MM-DD): ')
        if validate_date(date_text):
            break
        print('[!] Помилка! Введіть дату у форматі YYYY-MM-DD')

    while True:
        time_text = read_non_empty('Час (HH:MM): ')
        if validate_time(time_text):
            break
        print('[!] Помилка! Введіть час у форматі HH:MM')

    description = read_non_empty('Опис події: ')

    event_id = get_next_id(events)
    events[event_id] = {
        'title': title,
        'date': date_text,
        'time': time_text,
        'description': description,
        'completed': False
    }
    save_events(events)
    print('[OK] Подію додано')


def show_all_events(events):
    if not events:
        print('Подій немає')
        return

    for event_id in sorted(events, key=lambda eid: parse_event_datetime(events[eid])):
        event = events[event_id]
        print(f'ID: {event_id}')
        print(f'Назва: {event["title"]}')
        print(f'Дата: {event["date"]}')
        print(f'Час: {event["time"]}')
        print(f'Опис: {event["description"]}')
        print(f'Статус: {format_status(event)}')
        print()


def delete_event(events):
    if not events:
        print('Подій немає')
        return

    event_id = input('ID події для видалення: ').strip()
    try:
        if event_id in events:
            del events[event_id]
            save_events(events)
            print('[OK] Подію видалено')
        else:
            print('Подію не знайдено')
    except Exception as e:
        print(f'[!] Помилка при видаленні: {e}')


def edit_event(events):
    if not events:
        print('Подій немає')
        return

    event_id = input('ID події для редагування: ').strip()
    if event_id not in events:
        print('Подію не знайдено')
        return

    event = events[event_id]
    print('Залиште пустим, щоб не змінювати поле.')

    title = input(f'Назва [{event["title"]}]: ').strip() or event['title']

    while True:
        date_text = input(f'Дата [{event["date"]}] (YYYY-MM-DD): ').strip()
        if not date_text:
            date_text = event['date']
            break
        if validate_date(date_text):
            break
        print('[!] Помилка! Введіть дату у форматі YYYY-MM-DD')

    while True:
        time_text = input(f'Час [{event["time"]}] (HH:MM): ').strip()
        if not time_text:
            time_text = event['time']
            break
        if validate_time(time_text):
            break
        print('[!] Помилка! Введіть час у форматі HH:MM')

    description = input(f'Опис [{event["description"]}]: ').strip() or event['description']

    events[event_id] = {
        'title': title,
        'date': date_text,
        'time': time_text,
        'description': description,
        'completed': event.get('completed', False)
    }
    save_events(events)
    print('[OK] Подію оновлено')


def find_events_by_date(events):
    if not events:
        print('Подій на цю дату немає')
        return

    date_text = input('Введіть дату для пошуку (YYYY-MM-DD): ').strip()
    if not validate_date(date_text):
        print('[!] Помилка! Введіть дату у форматі YYYY-MM-DD')
        return

    matched = [event for event in events.values() if event.get('date') == date_text]

    if not matched:
        print('Подій на цю дату немає')
        return

    for event in sorted(matched, key=parse_event_datetime):
        print(f"{event['time']} — {event['title']} ({event['description']})")


def search_events_by_keyword(events):
    if not events:
        print('Подій немає')
        return

    keyword = input('Введіть ключове слово для пошуку: ').strip().lower()
    if not keyword:
        print('[!] Помилка! Значення не може бути пустим')
        return

    matched = [
        (event_id, event)
        for event_id, event in events.items()
        if keyword in event.get('title', '').lower() or keyword in event.get('description', '').lower()
    ]

    if not matched:
        print('Подій за ключовим словом не знайдено')
        return

    for event_id, event in sorted(matched, key=lambda item: parse_event_datetime(item[1])):
        print(f'ID: {event_id}')
        print(f'Назва: {event["title"]}')
        print(f'Дата: {event["date"]}')
        print(f'Час: {event["time"]}')
        print(f'Опис: {event["description"]}')
        print(f'Статус: {format_status(event)}')
        print()


def mark_event_completed(events):
    if not events:
        print('Подій немає')
        return

    event_id = input('ID події для позначення як виконаної: ').strip()
    if event_id not in events:
        print('Подію не знайдено')
        return

    if events[event_id].get('completed', False):
        print('Ця подія вже виконана')
        return

    events[event_id]['completed'] = True
    save_events(events)
    print('[OK] Подію позначено як виконану')


def show_next_event(events):
    if not events:
        print('Подій немає')
        return

    now = datetime.now()
    upcoming = [
        event
        for event in events.values()
        if not event.get('completed', False) and parse_event_datetime(event) >= now
    ]

    if not upcoming:
        print('Найближчої події немає')
        return

    next_event = min(upcoming, key=parse_event_datetime)
    print('Найближча подія:')
    print(f'Назва: {next_event["title"]}')
    print(f'Дата: {next_event["date"]}')
    print(f'Час: {next_event["time"]}')
    print(f'Опис: {next_event["description"]}')
    print(f'Статус: {format_status(next_event)}')


def show_menu():
    print('--- Персональний планувальник ---')
    print('1. Додати подію')
    print('2. Переглянути всі події')
    print('3. Видалити подію')
    print('4. Знайти події за датою')
    print('5. Редагувати подію')
    print('6. Пошук за ключовим словом')
    print('7. Позначити подію як виконану')
    print('8. Показати найближчу подію')
    print('9. Вийти')


def main():
    events = load_events()

    while True:
        show_menu()
        choice = input('Ваш вибір: ').strip()
        print()

        if choice == '1':
            add_event(events)
        elif choice == '2':
            show_all_events(events)
        elif choice == '3':
            delete_event(events)
        elif choice == '4':
            find_events_by_date(events)
        elif choice == '5':
            edit_event(events)
        elif choice == '6':
            search_events_by_keyword(events)
        elif choice == '7':
            mark_event_completed(events)
        elif choice == '8':
            show_next_event(events)
        elif choice == '9':
            print('До побачення!')
            break
        else:
            print('[!] Помилка! Оберіть пункт 1-9')

        print()


if __name__ == '__main__':
    main()
