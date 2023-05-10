def find_indices(arr, minimum, maximum):
    indices = []
    for i in range(len(arr)):
        if minimum <= arr[i] <= maximum:
            indices.append(i)
    return indices

# Пример использования
my_list = [10, 5, 7, 12, 8, 3, 9]
min_value = 5
max_value = 10

result = find_indices(my_list, min_value, max_value)
print("Индексы элементов в заданном диапазоне:")
print(result)