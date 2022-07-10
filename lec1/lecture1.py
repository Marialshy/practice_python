# print("hello world")
# является ли одно число квадратом другого:
# print("enter 1st number")
# a=int(input())
# print("enter 2nd number")
# b=int(input())
# if a*a==b:
#     print("yes")
# else:
#     print("no")


from decimal import MAX_EMAX


a = []
for i in range(5):
    x = int(input('-->'))
    a.append(x)
maxx = a[0]

for i in range(1, len(a)):
    if a[i] > maxx:
        maxx = a[i]

print(maxx)
