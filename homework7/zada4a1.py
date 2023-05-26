def check_rhythm(poem):
    # Разделяем стихотворение на фразы по пробелам
    phrases = poem.split()

    # Получаем количество слогов (гласных букв) в первой фразе
    syllables_count = count_syllables(phrases[0])

    # Проверяем количество слогов в остальных фразах
    for phrase in phrases[1:]:
        if count_syllables(phrase) != syllables_count:
            return "Пам парам"

    return "Парам пам-пам"

def count_syllables(phrase):
    # Разделяем фразу на слова по дефисам
    words = phrase.split("-")

    syllables_count = 0
    for word in words:
        # Подсчитываем количество гласных букв в слове
        syllables_count += count_vowels(word)

    return syllables_count

def count_vowels(word):
    vowels = "aeiouаеёиоуыэюя"
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

# Получаем стихотворение от пользователя
poem = input("Введите стихотворение Винни-Пуха: ")

# Проверяем ритм в стихотворении
result = check_rhythm(poem)
print(result)
