def find_divisible_numbers(a, b, c, k):
    divisible_numbers = []
    if a % k == 0:
        divisible_numbers.append(a)
    if b % k == 0:
        divisible_numbers.append(b)
    if c % k == 0:
        divisible_numbers.append(c)
    return divisible_numbers


a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))
k = int(input("Введіть число k (дільник): "))


divisible_numbers = find_divisible_numbers(a, b, c, k)
if divisible_numbers:
    print(f"Числа, які можна поділити на {k} без залишку: {divisible_numbers}")
else:
    print(f"Немає чисел, які можна поділити на {k} без залишку.")
