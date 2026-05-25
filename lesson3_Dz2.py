a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

choice = input("Оберіть дію (1 — сума, 2 — добуток): ")

if choice == "1":
    result = a + b + c
    print(f"Сума: {result}")
elif choice == "2":
    result = a * b * c
    print(f"Добуток: {result}")
else:
    print("Невірний вибір!")

a1 = float(input("Введіть перше число: "))
b1 = float(input("Введіть друге число: "))
c1   = float(input("Введіть третє число: "))

choice = input("Оберіть дію (1 — максимум, 2 — мінімум, 3 — середнє арифметичне): ")

if choice == "1":
    result = max(a1, b1, c1)
    print(f"Максимум: {result}")
elif choice == "2":
    result = min(a1, b1, c1)
    print(f"Мінімум: {result}")
elif choice == "3":
    result = (a1 + b1 + c1) / 3
    print(f"Середнє арифметичне: {result}")
else:
    print("Невірний вибір!")


grade = int(input("Введіть оцінку (1–5): "))

if grade == 1:
    print("Дуже погано")
elif grade == 2:
    print("Погано")
elif grade == 3:
    print("Задовільно")
elif grade == 4:
    print("Добре")
elif grade == 5:
    print("Відмінно")
else:
    print("Помилка! Оцінка має бути від 1 до 5.")



meters = float(input("Введіть кількість метрів: "))  

print("Оберіть варіант конвертації:")  
print("1 — Перевести в милі, дюйми або ярди (на вибір)")  
print("2 — Перевести одразу в милі, дюйми та ярди")  
print("3 — Перевести в кілометри та сантиметри")  

choice = input("Ваш вибір: ")  

if choice == "1":  
    print("Оберіть одиницю: 1 — милі, 2 — дюйми, 3 — ярди")  
    sub_choice = input("Ваш вибір: ")  
    if sub_choice == "1":  
        print(f"{meters} м = {meters / 1609.344:.4f} миль")  
    elif sub_choice == "2":  
        print(f"{meters} м = {meters * 39.3701:.2f} дюймів")  
    elif sub_choice == "3":  
        print(f"{meters} м = {meters * 1.09361:.2f} ярдів")  
    else:  
        print("Невірний вибір!")  

elif choice == "2":  
    miles = meters / 1609.344  
    inches = meters * 39.3701  
    yards = meters * 1.09361  
    print(f"{meters} м = {miles:.4f} миль")  
    print(f"{meters} м = {inches:.2f} дюймів")  
    print(f"{meters} м = {yards:.2f} ярдів")  

elif choice == "3":  
    km = meters / 1000  
    cm = meters * 100  
    print(f"{meters} м = {km} км")  
    print(f"{meters} м = {cm} см")  

else:  
    print("Невірний вибір!")


a2 = float(input("Введіть перше число: "))
b2 = float(input("Введіть друге число: "))

print("Оберіть операцію:")
print("1 — Додавання")
print("2 — Віднімання")
print("3 — Множення")
print("4 — Ділення")
print("5 — Залишок від ділення")
print("6 — Піднесення до степеня")

choice = input("Ваш вибір: ")

if choice == "1":
    print(f"{a2} + {b2} = {a2 + b2}")
elif choice == "2":
    print(f"{a2} - {b2} = {a2 - b2}")
elif choice == "3":
    print(f"{a2} * {b2} = {a2 * b2}")
elif choice == "4":
    if b2 != 0:
        print(f"{a2} / {b2} = {a2 / b2}")
    else:
        print("Помилка! Ділення на нуль.")
elif choice == "5":
    if b2 != 0:
        print(f"{a2} % {b2} = {a2 % b2}")
    else:
        print("Помилка! Ділення на нуль.")
elif choice == "6":
    print(f"{a2} ** {b2} = {a2 ** b2}")
else:
    print("Невірний вибір!")




num = int(input("Введіть тризначне число: "))

if 100 <= num <= 999:
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    if hundreds == tens == ones:
        print("Всі цифри однакові")
    elif hundreds == tens or hundreds == ones or tens == ones:
        print("Дві цифри однакові")
    else:
        print("Цифри різні")
else:
    print("Помилка! Введіть тризначне число.")