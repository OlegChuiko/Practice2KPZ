def closer_to_origin(x1, y1, x2, y2):
    dist1 = (x1 ** 2 + y1 ** 2) ** 0.5
    dist2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if dist1 < dist2:
        return "Точка А знаходиться ближче до початку координат."
    elif dist2 < dist1:
        return "Точка B знаходиться ближче до початку координат."
    else:
        return "Точки А і B рівновіддалені від початку координат."


x1 = float(input("Введіть координату x1: "))
y1 = float(input("Введіть координату y1: "))
x2 = float(input("Введіть координату x2: "))
y2 = float(input("Введіть координату y2: "))


result = closer_to_origin(x1, y1, x2, y2)
print(result)
44