def locate_point(x, y):
    if x == 0 and y == 0:
        return "Точка A знаходиться в початку координат."
    elif x == 0:
        return "Точка A знаходиться на осі Y."
    elif y == 0:
        return "Точка A знаходиться на осі X."
    else:
        if x > 0:
            if y > 0:
                return "Точка A знаходиться в першому квадранті."
            else:
                return "Точка A знаходиться в четвертому квадранті."
        else:
            if y > 0:
                return "Точка A знаходиться в другому квадранті."
            else:
                return "Точка A знаходиться в третьому квадранті."


x_coord = float(input("Введіть координату x точки A: "))
y_coord = float(input("Введіть координату y точки A: "))


location = locate_point(x_coord, y_coord)
print(location)
