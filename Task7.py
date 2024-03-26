def count_negative_numbers(a, b, c):
    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    return count


a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))


negative_count = count_negative_numbers(a, b, c)
print(f"Кількість негативних чисел: {negative_count}")
