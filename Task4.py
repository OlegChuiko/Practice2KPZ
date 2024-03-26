def replace_numbers(x, y):
    if x != y:
        if x < y:
            x = (x + y) / 2
            y = 2 * y
        else:
            y = (x + y) / 2
            x = 2 * x
    return x, y


x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))


result_x, result_y = replace_numbers(x, y)
print(f"Нове значення x: {result_x}")
print(f"Нове значення y: {result_y}")
