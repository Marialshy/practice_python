#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
print ('please enter number in range 1 - 7')
a = (input())
if a.isdigit() and int(a) in range(8):
    if 0 < int(a) < 6:
        print ('no, it\'s workday')
    else:
        print ('yeeees! weekend')
else:
    print ('failed, try again')
    