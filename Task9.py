def count_integer_numbers(a, b, c):
    count = 0
    if isinstance(a, int):
        count += 1
    if isinstance(b, int):
        count += 1
    if isinstance(c, int):
        count += 1
    return count


a = eval(input("Введіть число a: "))  
b = eval(input("Введіть число b: "))
c = eval(input("Введіть число c: "))


integer_count = count_integer_numbers(a, b, c)
print(f"Кількість цілих чисел: {integer_count}")
