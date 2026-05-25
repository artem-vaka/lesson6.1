import random
import time

players = [
    {"name": "Воїн",   "hp": 120, "max_hp": 120, "attack": 16, "defense": 10, "gold": 0, "inventory": ["меч", "щит"]},
    {"name": "Маг",    "hp": 80,  "max_hp": 80,  "attack": 25, "defense": 4,  "gold": 0, "inventory": ["посох", "книга заклинань"]},
    {"name": "Лучник", "hp": 100, "max_hp": 100, "attack": 18, "defense": 6,  "gold": 0, "inventory": ["лук", "стріли (20)"]},
    {"name": "Злодій", "hp": 90,  "max_hp": 90,  "attack": 20, "defense": 7,  "gold": 0, "inventory": ["кинджал", "відмички"]},
]

enemies = [
    {"name": "Гоблін",       "hp": 30,  "attack": 8,  "defense": 2,  "loot": "золота монета",  "loot_qty": 5},
    {"name": "Скелет",       "hp": 40,  "attack": 10, "defense": 4,  "loot": "золота монета",  "loot_qty": 8},
    {"name": "Темний лицар", "hp": 60,  "attack": 14, "defense": 8,  "loot": "золота монета",  "loot_qty": 15},
    {"name": "Дракон",       "hp": 100, "attack": 22, "defense": 10,  "loot": "золота монета",  "loot_qty": 40},
    {"name": "Лісовий дух",  "hp": 35,  "attack": 12, "defense": 3,  "loot": "золота монета",  "loot_qty": 10},
]

locations = [
    "Темний ліс — похмурі дерева шепочуть твоє ім'я...",
    "Стародавні руїни — вітер завиває між каменів.",
    "Гірський перевал — вузька стежка над прірвою.",
    "Підземелля — темрява огортає тебе з усіх боків.",
    "Чарівний сад — квіти світяться в нічній тиші.",
]

events = ["ворог", "скарб", "нічого", "торговець", "пастка", "ворог", "відпочинок"]

shop_items = ["зілля здоров'я", "чарівний амулет", "отруйний кинджал"]
shop_prices = [15, 30, 20]


def show_slow(text):
    print(text)
    time.sleep(0.5)


def show_fast(text):
    print(text)
    time.sleep(0.2)


def show_header(title):
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)
    time.sleep(0.3)


def choose_player():
    """Вивести список героїв і повернути вибраного."""
    show_header("ВИБІР ПЕРСОНАЖА")
    print("Обери свого героя:\n")

    for i, p in enumerate(players, 1):
        inv = ", ".join(p["inventory"])
        print(f"  {i}. {p['name']}")
        print(f"     HP: {p['hp']}  |  Атака: {p['attack']}  |  Захист: {p['defense']}")
        print(f"     Інвентар: {inv}")
        print()

    while True:
        choice = input("Введи номер (1-4): ")

        if choice == "1":
            player = dict(players[0])
            show_slow("\nТи обрав ВОЇНА! Міцний, витривалий, з мечем і щитом.")
            return player
        elif choice == "2":
            player = dict(players[1])
            show_slow("\nТи обрав МАГА! Слабкий тілом, але могутній магією.")
            return player
        elif choice == "3":
            player = dict(players[2])
            show_slow("\nТи обрав ЛУЧНИКА! Швидкий і влучний з лука.")
            return player
        elif choice == "4":
            player = dict(players[3])
            show_slow("\nТи обрав ЗЛОДІЯ! Спритний і хитрий, майстер відмичок.")
            return player
        else:
            print("Невірний вибір! Спробуй ще раз (1-4).")


def fight(player, enemy):
    enemy_copy = dict(enemy)
    enemy_copy["hp"] = enemy["hp"]

    show_slow(f"\n⚔️  Ти зустрів {enemy_copy['name']}! (HP: {enemy_copy['hp']})")

    while player["hp"] > 0 and enemy_copy["hp"] > 0:
        damage = player["attack"] - enemy_copy.get("defense", 0)
        if damage < 1:
            damage = 1
        enemy_copy["hp"] -= damage
        show_fast(
            f"   👊 Ти завдав {damage} шкоди {enemy_copy['name']}! "
            f"(Залишилось HP ворога: {max(0, enemy_copy['hp'])})"
        )

        if enemy_copy["hp"] <= 0:
            break

        enemy_damage = enemy_copy["attack"] - player["defense"]
        if enemy_damage < 1:
            enemy_damage = 1
        player["hp"] -= enemy_damage
        show_fast(
            f"   💥 {enemy_copy['name']} вдарив тебе на {enemy_damage}! "
            f"(Твоє HP: {max(0, player['hp'])})"
        )

    if player["hp"] <= 0:
        return False
    else:
        gold_reward = enemy_copy.get("loot_qty", 5)
        player["gold"] += gold_reward
        show_slow(f"\n🏆 Ти переміг {enemy_copy['name']}! +{gold_reward} золота!")
        return True


def shop(player):
    show_header("МАГАЗИН")
    show_slow("Торговець пропонує свої товари:")
    for idx, item in enumerate(shop_items, 1):
        print(f"  {idx}. {item} — {shop_prices[idx - 1]} золота")

    print(f"\nТвоє золото: {player['gold']}")
    print("  0. Вийти")

    while True:
        choice = input("Введи номер товару, який хочеш купити: ")
        if choice == "0":
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(shop_items):
            print("Невірний вибір. Спробуй ще раз.")
            continue

        index = int(choice) - 1
        price = shop_prices[index]
        item_name = shop_items[index]

        if player["gold"] < price:
            show_slow("У тебе недостатньо золота для покупки.")
            continue

        player["gold"] -= price
        player["inventory"].append(item_name)
        show_slow(f"Ти купив {item_name} за {price} золота.")
        break


def handle_event(player, event):
    """Обробити випадкову подію."""
    if event == "ворог":
        enemy = random.choice(enemies)
        return fight(player, enemy)
    elif event == "скарб":
        gold_found = random.randint(10, 30)
        player["gold"] += gold_found
        show_slow(f"\n💎 Ти знайшов скарб! +{gold_found} золота!")
        return True
    elif event == "нічого":
        show_slow("\n🌿 Нічого цікавого... Тільки вітер і тиша.")
        return True
    elif event == "торговець":
        show_slow("\n🧙 Мандрівний торговець з'явився з нізвідки!")
        shop(player)
        return True
    elif event == "пастка":
        trap_damage = random.randint(10, 25)
        player["hp"] -= trap_damage
        show_slow(
            f"\n⚠️  Пастка! Ти втратив {trap_damage} HP! "
            f"(Залишилось: {max(0, player['hp'])})"
        )
        return player["hp"] > 0
    elif event == "відпочинок":
        heal = random.randint(15, 35)
        player["hp"] += heal
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
        show_slow(f"\n😌 Відпочинок повернув тобі {heal} HP. Тепер у тебе {player['hp']} HP.")
        return True
    else:
        show_slow("\nНічого не сталося.")
        return True


def choose_location():
    show_header("ОБЕРИ ЛОКАЦІЮ")
    for idx, location in enumerate(locations, 1):
        print(f"  {idx}. {location}")

    while True:
        choice = input("Введи номер локації: ")
        if choice.isdigit() and 1 <= int(choice) <= len(locations):
            return int(choice) - 1
        print("Невірний вибір. Спробуй ще раз.")


def show_status(player):
    show_header("СТАТУС ГЕРОЯ")
    show_slow(f"Герой: {player['name']}")
    show_slow(f"HP: {player['hp']} / {player['max_hp']}")
    show_slow(f"Золото: {player['gold']}")
    show_slow(f"Інвентар: {', '.join(player['inventory'])}")


def choose_action():
    print("\nЩо ти хочеш зробити?")
    print("  1. Дослідити локацію")
    print("  2. Відпочити")
    print("  3. Перевірити інвентар")
    print("  4. Переглянути статус")
    print("  0. Вийти з пригоди")

    while True:
        choice = input("Введи номер дії: ")
        if choice in {"0", "1", "2", "3", "4"}:
            return choice
        print("Невірний вибір. Спробуй ще раз.")


def explore_location(player, location_num):
    while True:
        entry_action = choose_action()
        if entry_action == "0":
            show_slow("\nТи вирішив завершити пригоду раніше.")
            return False
        if entry_action == "1":
            break
        if entry_action == "2":
            heal = random.randint(10, 20)
            player["hp"] += heal
            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]
            show_slow(f"\n😌 Ти відпочив і відновив {heal} HP. Тепер у тебе {player['hp']} HP.")
            continue
        if entry_action == "3":
            show_header("ІНВЕНТАР")
            show_slow(f"Інвентар: {', '.join(player['inventory'])}")
            continue
        if entry_action == "4":
            show_status(player)
            continue

    location_index = location_num - 1
    show_header(f"ЛОКАЦІЯ {location_num}")
    show_slow(locations[location_index])
    if random.random() < 0.5:
        event = "ворог"
    else:
        non_enemy_events = [e for e in events if e != "ворог"]
        event = random.choice(non_enemy_events) if non_enemy_events else "нічого"

    if not handle_event(player, event):
        return False
    return True


def main():
    """Головна функція — запуск гри."""
    show_header("ЛАСКАВО ПРОСИМО В ПІДЗЕМЕЛЛЯ ДОЛІ!")
    show_slow("Ти — шукач пригод, що стоїть перед брамою невідомості...")

    player = choose_player()
    show_slow(f"\nГерой {player['name']} вирушає в путь!")
    show_slow(f"Твій інвентар: {', '.join(player['inventory'])}")
    show_slow("Попереду на тебе чекають 5 випробувань...")

    time.sleep(1)
    show_header("ГРА ПОЧИНАЄТЬСЯ!")

    game_completed = False
    for location_num in range(1, 6):
        if not explore_location(player, location_num):
            show_slow("\nГру завершено.")
            break
        if location_num < 5:
            show_slow(f"\nПісля випробування ти маєш {player['hp']} HP і {player['gold']} золота.")
    else:
        show_slow("\nВітаємо! Ти пройшов всі 5 випробувань і дійшов до Чарівного саду!")
        game_completed = True

    show_header("РЕЗУЛЬТАТ")
    show_slow(f"Герой: {player['name']}")
    show_slow(f"HP: {player['hp']} / {player['max_hp']}")
    show_slow(f"Золото: {player['gold']}")
    show_slow(f"Інвентар: {', '.join(player['inventory'])}")


if __name__ == "__main__":
    main()
