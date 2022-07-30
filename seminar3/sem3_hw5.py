#список чисел Фибоначчи, в том числе для отрицательных индексов
k = int(input("please enter count of elements: "))
def fibonacci (a: int):
    list_fibo = [0,1]
    for i in range(2,a+1):
        new_el = list_fibo[i-1]+list_fibo[i-2]
        list_fibo.append(new_el)
    return list_fibo

def nega_list(any_list: list):
    new_list = []
    for i in range(1,len(any_list)-1):
        new_el = any_list[-i]
        if len(any_list)%2<1 and i%2<1:
            new_el=-new_el
        elif len(any_list)%2>=1 and i%2>=1:
            new_el=-new_el
        new_list.append(new_el)
    return new_list+any_list

print(nega_list(fibonacci(k)))