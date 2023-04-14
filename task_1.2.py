# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import random

# выберем три случайные песни
selected_songs = random.sample(my_favorite_songs, 3)

# вычислим общее время звучания трех песен
total_duration = 0
for song in selected_songs:
    total_duration += song[1]

# выведем результат в формате "Три песни звучат ХХХ минут"
print(f"Три песни звучат {total_duration:.0f} минут")

import random

# выберем три случайные песни
selected_songs = random.sample(list(my_favorite_songs_dict.items()), 3)

# вычислим общее время звучания трех песен
total_duration = 0
for song in selected_songs:
    total_duration += song[1]

# выведем результат в формате "Три песни звучат ХХХ минут"
print(f"Три песни звучат {total_duration:.0f} минут")