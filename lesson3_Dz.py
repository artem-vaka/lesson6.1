num1 = float(input("Введіть число: "))
if num1 > 0:
    print("Додатнє")
elif num1 < 0:
    print("Від'ємне")
else:
    print("Нуль")



age = int(input("Скільки вам років? "))
if 0 <= age <= 5:
    print("Малюк")
elif 6 <= age <= 17:
    print("Школяр")
elif 18 <= age <= 23:
    print("Студент")
elif 24 <= age <= 60:
    print("Дорослий")
elif age >= 61:
    print("Сеньйор")
else:
    print("Некоректний вік")


password = input("Введіть пароль: ")
if password == "admin123":
    print("Вхід дозволено")
else:
    print("Невірний пароль")



temp = float(input("Введіть температуру (°C): "))
if temp < 0:
    print("Мороз")
elif 0 <= temp <= 20:
    print("Прохолодно")
elif 21 <= temp <= 30:

    if temp == 30:
        print("Спека")
    else:
        print("Тепло")
else:  # temp > 30
    print("Спека")


balance = float(input("Введіть баланс грошей: "))
card = input("Чи є картка лояльності? (так/ні): ").strip().lower()

if balance > 5000 and card == "так":
    print("VIP клієнт")
else:
    print("Звичайний клієнт")



num6 = int(input("Введіть число: "))
if num6 % 10 == 0:
    print("Число особливе")
elif num6 % 2 == 0:
    print("Парне")
else:
    print("Непарне")