# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

your_array = [el for el in input("Введите массив данных для проверки: ").split()]

def unic():
    your_array
    unic = []
    
    for i, word1 in enumerate(your_array):
        count= 0
        for word2 in your_array[i + 1:]:
            if word2 in word1:
                count += 1         
        if count>0:
            unic.append(your_array[i])
    print(set(unic))
    
unic()

   








