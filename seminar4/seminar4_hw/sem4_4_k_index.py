#натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random as r
k = int(input("please enter number for k: "))
path = r'seminar4/seminar4_hw/polynomial.txt'
with open(path, 'a') as f:
    for i in range((k+1)):
        a = r.randint(0,100)
        if a==0: pass
        else:
            if k>1: 
                f.write((f'{a}*x^{k} + '))
            elif k==1: 
                f.write(f'{a}*x')
            else: 
                f.write(f'+ {a}')
        k-=1
    f.write(' = 0')
    f.write('\n')
with open(path, 'r') as f:
    read_me = f.read()
print(read_me)
    

# def create_polynomial(b:int):
#     new_list=[]
#     for i in range((k+1)):
#         a = r.randint(0,10)
#         if a==0: pass
#         else:
#             if b>1: 
#                 new_list.append(f'{a}*x^{b} + ')
#             elif b==1: 
#                 new_list.append(f'{a}*x')
#             else: 
#                 new_list.append(f'+ {a}')
#         b-=1
#     new_list.append(' = 0')
#     return new_list

# print(create_polynomial(k))