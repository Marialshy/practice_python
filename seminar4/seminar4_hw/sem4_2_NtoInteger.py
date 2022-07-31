# Вводится натуральное число N. Программа составит список простых множителей числа N.
import math
some_number=int(input("please enter number: "))
def find_prime_numbers(n:int):
    list_integers = []
    for i in range(2,int(math.sqrt(n))):
        while n%i==0:
            n=n/i
            list_integers.append(int(i))
        if n/i!=1:
            list_integers.append(int(n))
    return list_integers
print(find_prime_numbers(some_number))