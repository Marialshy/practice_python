#программа принимает на вход число N и выдает набор произведений чисел от 1 до N.
number=int(input("please enter number: "))
def find_factorial_range(nmbr: int):
    some_list=[]
    new_nmbr = 1
    for i in range(1,nmbr):
        new_nmbr = i*new_nmbr
        some_list.append(new_nmbr)
    return some_list
print(find_factorial_range(number))