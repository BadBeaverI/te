import random
n = int(input())   # вводим количество элементов в массиве
a = [random.randint(0, 10) for i in range(n)]   # вводим элементы массива
print (a)
x = int(input())   # вводим число, которое нужно найти в массиве

count = 0   # счетчик вхождений числа X в массив

for i in range(n):
    if a[i] == x:
        count += 1

print(count)