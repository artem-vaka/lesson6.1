uah = float(input(" Введіть суму в гривнях: "))  
print(f"{uah} грн = {uah/41.5} USD")  
print(f"{uah} грн = {uah/45.0} EUR")  
print(f"{uah} грн = {uah/10.5} PLN") 




a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть операцію (+, -, *, /, %, **): ")

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    print(f"{a} / {b} = {a / b}")
elif op == "%":
    print(f"{a} % {b} = {a % b}")
elif op == "**":
    print(f"{a} ** {b} = {a ** b}")
else:
    print("Невідома операція")




sentence = input("Введіть речення: ")

words = sentence.split()
word_count = len(words)
letter_count = sum(1 for ch in sentence if ch.isalpha())

print(f"Кількість слів: {word_count}")
print(f"Кількість букв: {letter_count}")
print(f"Верхній регістр: {sentence.upper()}")
#в цьому завданні звернувся до ші бо непрацювало чомусь letter_count


year = int(input("Введіть рік: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} — високосний рік")
else:
    print(f"{year} — не високосний рік")

    

num = input("Введіть число: ")

total = sum(int(digit) for digit in num)

print(f"Сума цифр числа {num} = {total}")