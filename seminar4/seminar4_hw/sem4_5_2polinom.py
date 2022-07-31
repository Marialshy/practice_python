#Программа формирует файл, содержащий сумму многочленов, взятых из двух других файлов.
path1 = r'seminar4/seminar4_hw/polynomial.txt'
path2 = r'seminar4/seminar4_hw/2polynom.txt'

with open(path1, 'r') as f:
    list_1 = f.readlines() #считывает в список, при этом есть символ новой строки:['2*x^3 + x^2 = 0\n', '3*x ...
with open(path2, 'r') as f:
    list_2 = f.readlines()

def convert_countable(sm_list: list, i:int, split_symb: str=' '):
    new_str=''
    new_str=str.split(sm_list[i],split_symb)
    return new_str
    
print(list_1)
print(list_2)

polymn_1=convert_countable(list_1,0)
polymn_2=convert_countable(list_2,0)

# element1=convert_countable(polymn_1,0,'^')
# element2=convert_countable(polymn_2,0,'^')
# if element1[1]==element2[1]:
#     new_str=str.split(element1[0],'*x')
#     new_str2=str.split(element2[0],'*x')
#     new_a=int(new_str[0])+int(new_str2[0])
# print(new_a)