#Задана последовательность чисел. Программа формирует список неповторяющихся элементов исходной последовательности.
some_list=str.split(input("please enter numbers, using split: "))
def create_without_duplicates(text: list):
    new_list =[]
    for i in range (len(text)):
        if int(text[i]) in new_list:
            pass
        else:
            new_list.append(int(text[i]))
    return new_list
print(create_without_duplicates(some_list))