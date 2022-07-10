#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# корень из суммы квадратов (x_b - x_a) и (y_b - y_a)
x_a = int(input('enter X-axis coordinate for A:'))
y_a = int(input('enter Y-axis coordinate for A:'))
x_b = int(input('enter X-axis coordinate for B:'))
y_b = int(input('enter Y-axis coordinate for B:'))

import math
distance_ab = math.sqrt((x_b - x_a)**2+(y_b - y_a)**2)
print(f"distance A-B = {round(float(distance_ab),2)}")