# Получаем данные от пользователя
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

# Создаем пустой массив для хранения прогрессии
progression = []

# Заполняем массив арифметической прогрессией
for i in range(n):
    element = a1 + (i * d)
    progression.append(element)

# Выводим массив прогрессии
print("Арифметическая прогрессия:")
for element in progression:
    print(element)
