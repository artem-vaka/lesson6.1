sentence = input("Введіть речення: ")
words = sentence.split()

word_counts = {}
for word in words:
    normalized = word.lower()
    word_counts[normalized] = word_counts.get(normalized, 0) + 1

print("Список слів:", words)
print("Кількість кожного слова:")
for word, count in word_counts.items():
    print(f"{word}: {count}")