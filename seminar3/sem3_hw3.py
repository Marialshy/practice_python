#список из вещественных чисел. Программа находит разницу между максимальным и минимальным значением дробной части элементов.
some_list=str.split(input("please enter numbers, using split: "))

def find_fractional_part(list_1: list):
    find_list=[]
    for i in range(0,len(list_1)):
        if float(list_1[i])*10%10>=1:# это работает только для сравнения чисел, где сразу после запятой не 0
            new_elenment = str.split(list_1[i],".")
            find_list.append(int(new_elenment[1]))
        elif 0<float(list_1[i])*10%10<1:# а если будет число типа 0,00... - нужно бы докрутить логику
                new_elenment = str.split(list_1[i],".")
                find_list.append(float(int(new_elenment[1])/10))
    return find_list

def find_max_2(list_1: list):
    max_num = list_1[0]
    max_num2 = list_1[1]
    for i in range(1, len(list_1)):
        if list_1[i] > max_num:
            max_num2 = max_num
            max_num = list_1[i]
    return max_num-max_num2
    
print(find_max_2(find_fractional_part(some_list)))