word = input("Введите слово из маленьких латинских букв: ")

vowels = "aeiou"
count_vowels = 0
count_consonants = 0

# Подсчёт гласных и согласных
for ch in word:
    if ch in vowels:
        count_vowels += 1
    elif ch.isalpha():  # считаем остальные буквы латинскими согласными
        count_consonants += 1

print(f"Количество гласных: {count_vowels}")
print(f"Количество согласных: {count_consonants}")

# Подсчёт каждой из гласных букв
vowel_counts = {v: word.count(v) for v in vowels}

# Проверка: если какой-то из гласных букв нет — выводим False
if any(count == 0 for count in vowel_counts.values()):
    print(False)
else:
    # Если все гласные есть, можно вывести их количества (по желанию)
    print(vowel_counts)