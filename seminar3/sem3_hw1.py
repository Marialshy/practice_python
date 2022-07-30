#Задайте список из нескольких чисел. Программа находит сумму элементов списка, стоящих на нечётной позиции.
some_list=str.split(input("please enter numbers, using split: ")) # .split() разделяет основную строку по разделителю и возвращает список строк.
def find_sum_elements(list_1: list):
    result = 0
    for i in range(1,len(list_1),2): #шаг 2
        result+=int(list_1[i])
    return result     

print(f'sum of uneven elements = {find_sum_elements(some_list)}')