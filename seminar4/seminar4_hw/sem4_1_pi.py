#Вычислить число c заданной точностью d, 10^{-1} ≤ d ≤10^{-10}
d = int(input("введите число знаков после запятой: "))
path = r'seminar4/seminar4_hw/3,14.txt'
with open(path,'r') as pi:
    data_pi = float(pi.read(5+d))
print(round(data_pi,d))

#если d получен в формате 0.001:
d = (input("введите число в нужном формате: ")) # или считать с файла например вместо ввода
path = r'seminar4/seminar4_hw/3,14.txt'
with open(path,'r') as pi:
    new_d = str.split(d,".")
    count = 0
    for i in range(len(new_d[1])):
        count +=i
    data_pi2 = float(pi.read(5+count))
print(round(data_pi2,count))