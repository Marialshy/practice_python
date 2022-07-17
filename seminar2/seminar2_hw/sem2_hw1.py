#программа принимает на вход вещественное число и показывает сумму его цифр.

number=float(input('please enter number: '))
def count_digit_sum(num:float):
    sum_num = 0
    if num>=1:
        while num%10>0:
            sum_num +=int(num%10)
            num=int(num/10)
    else:
        if num<0:
            num=-num
        while num%10!=0:
            sum_num +=int(num%10)
            num=num*10
    return sum_num

print(f"digit sum for {number} = {count_digit_sum(number)}")
