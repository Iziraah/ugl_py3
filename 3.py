# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

stuff = [
    {'спички': 0.5},
    {'сковорода': 3},
    {'котелок': 5},
    {'тушенка': 2},
    {'сачек': 1},
    {'велосипед': 10},
    {'нож': 1},
]
backpack = int(input('ВВедите вместительность рюкзака: '))
need_stuff = []
sum = 0
for stuffs in stuff:
    for key, value in stuffs.items():
        if sum + value < backpack:
            need_stuff.append(stuffs)
            sum += value
print(need_stuff)

