# Программа находит произведение пар чисел списка (первый и последний элемент, второй и предпоследний и т.д.)
some_list=str.split(input("please enter numbers, using split: "))
def find_lehgnt(any_list: list):
    if len(any_list)%2<1:
        return int(len(any_list)/2)
    else:
        return int(len(any_list)/2+1)

def find_multy_elements(list_1: list):
    result = 1
    result_list=[]
    for i in range(0,find_lehgnt(list_1)):
        result=int(list_1[i])*int(list_1[-(i+1)]) #-1:индекс последнего элемента
        result_list.append(result) 
    return result_list     

print(f'new list : {find_multy_elements(some_list)}')