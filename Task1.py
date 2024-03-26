def square_or_power(num):
    if num >= 0:
        return num ** 2
    else:
        return num ** 4

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

result1 = square_or_power(num1)
result2 = square_or_power(num2)
result3 = square_or_power(num3)

print(f"Результат для першого числа: {result1}")
print(f"Результат для другого числа: {result2}")
print(f"Результат для третього числа: {result3}")
