def is_triangle_possible(angle1, angle2):
    if angle1 + angle2 < 180:
        return True
    else:
        return False

def is_right_triangle(angle1, angle2):
    if angle1 == 90 or angle2 == 90 or angle1 + angle2 == 90:
        return True
    else:
        return False


angle1 = float(input("Введіть перший кут трикутника (в градусах): "))
angle2 = float(input("Введіть другий кут трикутника (в градусах): "))


if is_triangle_possible(angle1, angle2):
    print("Такий трикутник існує.")
    if is_right_triangle(angle1, angle2):
        print("Трикутник є прямокутним.")
    else:
        print("Трикутник не є прямокутним.")
else:
    print("Такий трикутник не існує.")