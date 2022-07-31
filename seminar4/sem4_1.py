#считать строку из файла, найти наибольшее число (разделитель - пробел)
path = r'seminar4/file.txt'
#with open (path, 'a') as f:
#    f.write(input("please enter numbers, using split: "))
def find_max(list_1: list):
    max_num = int(list_1[0])
    for i in range(1, len(list_1)):
        if int(list_1[i]) > int(max_num):
            max_num = list_1[i]
    return max_num

with open (path, 'r') as f:
    some_list=str.split(f.read())
    print(find_max(some_list))


