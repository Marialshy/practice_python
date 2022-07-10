#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
#и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
a_x = int(input('enter X-axis coordinate:'))
a_y = int(input('enter Y-axis coordinate:'))

if a_x == 0 and a_y == 0:
    print("failed, try again")
elif a_x == 0:
    print(f"A({a_x},{a_y}) is at X-axis")
elif a_y == 0:
    print(f"A({a_x},{a_y}) is at Y-axis")
elif a_x > 0:
    if a_y > 0:
        print(f"A({a_x},{a_y}) is at Quadrant I")
    elif a_y < 0:
        print(f"A({a_x},{a_y}) is at Quadrant IV")
elif a_x < 0:
    if a_y < 0:
        print(f"A({a_x},{a_y}) is at Quadrant III")
    elif a_y > 0:
        print(f"A({a_x},{a_y}) is at Quadrant II")
