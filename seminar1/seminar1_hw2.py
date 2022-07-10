#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# для тернарной (трёхоперандной) дизъюнкции только если все три 0, ответ 0

import random

x = random.randint(0,1)
y = random.randint(0,1)
z = random.randint(0,1)

if x==y==z==0:
    left_side_part = 1
else:
    left_side_part = 0

right_side_part = not(x and y and z)

print(f"{x},{y},{z}")
print(f"{right_side_part == left_side_part}")


