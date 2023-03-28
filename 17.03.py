import random
k = 5
y = []
while k != 0:
    x = random.randint (1, 6)
    k -= 1
    y.append(x)
    print (y)
total = sum(y)
print ("Сумма бросков составляет", total)

import random
chars = '!@#$%^&*()_+:?><qwertyuiop[]asdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
lenght = input('Длинна пароля' + '\n')
password = ''
try:
    lenght = int(lenght)
    for n in range(lenght):
        password += random.choice(chars)
    print (password)
except ValueError:
    print ('Дибил, введи число цифрами!!!')
    lenght = input('Длинна пароля' + '\n')
    lenght = int(lenght)
    for n in range(lenght):
        password += random.choice(chars)
    print (password)


# Сортировка !!!

arr = [12, 4, 54, 29, 46, 36, 72, 99, 85]

# 1 вариант
n = len(arr)
print ('Длинна массива', n)
i = 0
while i < n - 1:
    m = i
    j = i + 1
    while j < n:
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print (arr)

# 2 вариант
print (sorted(arr))

# 3 вариант Сортировка пузырьком
arr = [7, 5, 3, 9, 14, 24, 48, 54, 13, 27, 29]
n = len(arr)

for i in range(n-1):
    for j in range (n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# 4 вариант Сортировка пузырьком
arr = [7, 5, 3, 9, 14, 24, 48, 54, 13, 27, 29]
n = len(arr)

i = 0
while i < n -1:
    j = 0
    while j < n-1-i:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        j += 1
    i += 1
print(arr)



from random import randint

n = 10
arr = []
# создание рандомного массива
for i in range (n):
     arr.append(randint(1,100))
print (arr)
# # сортировка рандомного массива
for i in range(n-1):
      for j in range (n-i-1):
          if arr[j] > arr[j+1]:
             arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)


# Бинарный поиск
# Объявим функцию
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        # Если элемент в середине
        if arr[mid] == x:
            return mid
        # Если элемент не в середине, то проверяем левую часть
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Если элемент в правой части массива
        else:
            return binary_search(arr, mid + 1, high, x)
    # Если элемент вообще не в массиве
    else:
        return -1
    
# Тестовый массив
arr = [6, 8, 11, 13, 25, 27, 44, 66, 72, 74, 83, 88, 91, 96, 101, 106]
x = input("Введите число: ")
x = int(x)

# Вызов функции
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Элемент найден в массиве под индексом", str(result))
else:
    print("Элемент не присутствует в массиве")
