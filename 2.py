# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

from itertools import groupby
import re


# your_array = input("Введите массив данных для проверки: \n")
# your_array = (re.sub(r'[.,"\'-?:!;]', '', your_array)).split()

your_array = [el for el in input("Введите массив данных для проверки: ").split()]

def unic():
    your_array
    unic = {}
        
    for i, elem1 in enumerate(your_array):
        count = 0
        for elem2 in your_array[i - 1::-1]:
            if elem2 == elem1:
                count += 1
        if count>0:      
            dict = {your_array[i]:count+1}
            unic.update(dict)
    return unic

unic_dict = unic()
print(unic_dict)
values = []
for key, value in unic_dict.items():
        values.append(value)
values.sort()
values.reverse()
values = values[10:]
values_finish = [el for el, _ in groupby(values)]
unic_dict_copy = unic_dict.copy()
for i in range(len(values_finish)):
    get = values_finish[i]
    # print(get)
    for key, val in unic_dict.items():
        if val == get:
            del unic_dict_copy[key]

print(unic_dict_copy)

unic()
