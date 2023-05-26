def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = ""
        for j in range(1, num_columns + 1):
            value = operation(i, j)
            row += str(value) + " "
        print(row.strip())

# Пример использования функции с операцией умножения
print_operation_table(lambda x, y: x * y)
