def rythm(poem):
    syllables = [] # список с количеством слогов в каждой фразе
    for phrase in poem:
        vowels = [letter for letter in phrase if letter in 'аоиеёэыуюя'] # оставляем только гласные буквы
        # count_vowels = sum([1 for letter in phrase if letter in 'аоиеёэыуюя'])
        syllables.append(len(vowels)) # определяем число слогов и добавляем в список
    if len(set(syllables)) == 1: # если все числа в списке одинаковы
        return True
    return False

poem = input('Введите стихотворение ').split() 
# poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'.split()
if rythm(poem):
    print('Парам пам-пам')
else:
    print('Пам-парам')