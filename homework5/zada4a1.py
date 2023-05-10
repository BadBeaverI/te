def power_recursive(a, b):
    # Базовый случай: если степень равна 0, возвращаем 1
    if b == 0:
        return 1

    # Рекурсивный случай: возводим число A в степень B-1 и умножаем на A
    return a * power_recursive(a, b - 1)

# Получаем входные числа от пользователя
a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

# Вызываем функцию power_recursive и выводим результат
result = power_recursive(a, b)
print(f"Результат: {result}")
