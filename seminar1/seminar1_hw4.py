#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
a = int(input('please enter quadrant'))
if a in range(1,5):
    if a == 1:
        print(f'for A(x,y) in Q{a}: x > 0, y > 0')
    elif a == 2:
        print(f'for A(x,y) in Q{a}: x < 0, y > 0')
    elif a == 3:
        print(f'for A(x,y) in Q{a}: x < 0, y < 0')
    elif a == 4:
        print(f'for A(x,y) in Q{a}: x > 0, y < 0')
else:
    print ('failed, try again')
    