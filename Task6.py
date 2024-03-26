def replace_numbers(a, b):
    if a != b:
        max_num = max(a, b)
        a = max_num
        b = max_num
    else:
        a = 0
        b = 0
    return a, b


a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))


result_a, result_b = replace_numbers(a, b)
print(f"Нове значення a: {result_a}")
print(f"Нове значення b: {result_b}")
