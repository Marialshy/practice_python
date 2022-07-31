#Вычислить число c заданной точностью d, 10^{-1} ≤ d ≤10^{-10}
d = int(input("введите число знаков после запятой: "))
path = r'seminar4/seminar4_hw/3,14.txt'
with open(path,'r') as pi:
    data_pi = float(pi.read(5+d))
print(round(data_pi,d))

