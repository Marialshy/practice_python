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
    new_list = any_list
    index =0
    index_list=[]
    
    for i in range(len(any_list)): 
        while index_list.count(i) !=1:
            index_n = random.randint(0,len(any_list)-1)
            print(index_n)
            index_list.append(index_n)
            print(index_list)
            new_list[i]= any_list[index-1]
            print(new_list)
    return new_list

print(list_mix(fill_list_n_range(number)))