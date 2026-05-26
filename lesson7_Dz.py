def calc(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Ділення на нуль!"
        return a / b
    else:
        return "Невідома операція"

print("Функція calc:")
print(f"10 + 5 = {calc(10, 5, '+')}")
print(f"10 - 5 = {calc(10, 5, '-')}")
print(f"10 * 5 = {calc(10, 5, '*')}")
print(f"10 / 5 = {calc(10, 5, '/')}")
print()


last_digit = lambda x: x % 10

print("Остання цифра числа:")
print(f"Остання цифра 12345: {last_digit(12345)}")
print(f"Остання цифра 789: {last_digit(789)}")
print()


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

print("Квадрати чисел:")
print(f"Числа: {numbers}")
print(f"Квадрати: {squares}")
print()


words = ["python", "java", "javascript", "c", "golang", "rust"]
long_words = list(filter(lambda word: len(word) > 5, words))

print("Слова довші за 5 символів:")
print(f"Усі слова: {words}")
print(f"Довгі слова: {long_words}")
print()


students = [
    {"name": "Ivan", "age": 18},
    {"name": "Olya", "age": 20},
    {"name": "Max", "age": 17}
]

sorted_students = sorted(students, lambda student: student["age"])

print("Студенти відсортовані за віком:")
print(f"Оригінальний список: {students}")
print(f"Відсортований список:")
for student in sorted_students:
    print(f"  - {student['name']}: {student['age']} років")
