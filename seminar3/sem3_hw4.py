#программа преобразовывает десятичное число в двоичное
num =int(input("please enter number: "))
bin_num = ''
while num > 0:
    bin_num = str(num % 2) + bin_num
    num = num // 2
print(f'->{bin_num}')