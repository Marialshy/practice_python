#алгоритм перемешивания списка (пусть список из задачи 4) - random.shuffle(<Список>)
import random
number=int(input("please enter number: "))

def fill_list_n_range(nmbr: int):
    some_list=[]
    for i in range(-nmbr,nmbr+1):
        some_list.append(i)
    return some_list
print(fill_list_n_range(number))

def list_mix(any_list: list):
    new_list = []
    while len(new_list)<len(any_list):
            index = random.randint(0,len(any_list)-1)
            if any_list[index] in new_list:
                pass
            else:
                new_list.append(any_list[index])
    return new_list

print(list_mix(fill_list_n_range(number)))
