# Пользователь задает N, и для списка из N элементов, заполненных числами из промежутка [-N, N]
# программа находит произведение элементов на указанных позициях (вводит пользователь)
number=int(input("please enter number: "))

def fill_list_n_range(nmbr: int):
    some_list=[]
    for i in range(-nmbr,nmbr+1):
        some_list.append(i)
    return some_list

index_a=int(input("please enter index for the first element: "))
index_b=int(input("please enter index for the second element: "))

def count_multiply(numb_1: int,numb_2: int, any_list: list):
    answer_multy = any_list[numb_1]*any_list[numb_2]
    return answer_multy

print(f'element[{index_a}]*element[{index_b}] = {count_multiply(index_a, index_b, fill_list_n_range(number))}')