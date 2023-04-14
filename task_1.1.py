# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

print (my_favorite_songs [0:14] + my_favorite_songs [-14:-1] + my_favorite_songs [15:30] + my_favorite_songs [-27:-15])

# разбиваем строку на список строк, используя запятую как разделитель
songs_list = my_favorite_songs.split(',')

# выводим на консоль первый трек
print(songs_list[0])

# выводим на консоль последний трек
print(songs_list[-1])

# выводим на консоль второй трек
print(songs_list[1])

# выводим на консоль второй с конца трек
print(songs_list[-2])