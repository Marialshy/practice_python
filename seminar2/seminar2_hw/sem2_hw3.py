#сумма для списка из n чисел последовательности (1 + 1/n)^n
number=int(input("please enter number: "))
def count_sum_for_n(n: int):
    sum_n = 0
    for i in range(n):
        sum_n+=(1 + 1/n)**n
    return sum_n
print(count_sum_for_n(number))