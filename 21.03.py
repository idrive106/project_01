# # 1

# salary = float(input('Введите зарплату '))
# expenses = float(input('Введите расходы '))
# months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# tempexp = expenses
# tempsal = salary
# if salary <= expenses:
#     print('Поданы не правильные данные в программу')
# else:
#     for i in months:
#         print('Сейчас месяц ', i)
#         if i != 1:
#             salary = salary * 1.05
#             tempsal = tempsal + salary
#             print('Зарплата:', tempsal)
#             tempexp = expenses * i
#             print('Расходы: ', tempexp)
#         else:
#             print('Первый месяц без процентов')
#             print(salary, expenses)
# live = abs(tempsal - tempexp)
# print ('Сотрудник накопит', round(live,2), 'рублей')


# # 2

# arr = [-3, 2, 4, 0, 5]
# k = 9
# result = []

# for x in arr:
#     for y in arr:
#        if x + y == k:
#         result.append([x, y])
# print(result)


# еще один способ не работает!!!

arr = [-3,2,4,0,5]
k = 4
result = []

low = 0
high = len(arr)-1

while low < high:
    sum = arr[low] + arr[high]
    if sum == k:
        result.append([arr[low], arr[high]])
    if sum < k:
        low += 1
    else:
        high -= 1
print(result)

# Бинарный поиск
def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    index = -1
    while (low <= high) and (index == -1):
        mid = (low+high) // 2
        if arr[mid] == x:
            index = mid
        else:
            if x < arr[mid]:
                low = mid -1
            else:
                low = mid +1
    return index
# Экспоненциальный поиск
def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= x:
        index = index * 2
    return binary_search( arr[:min(index, len(arr))], x)
# Тестовый массив
arr = [3,4,5,6,7,8,9]
x = int(input('Введи цифру: '))
# Вызов функции
print("Индекс искомого элемента: ",(exponential_search(arr,x)))

# Jump Search

import math
from random import randint

def JumpSearh(arr,value):
  length = len(arr)
  jump = int(math.sqrt(length))
  left = 0
  rigth = 0
  while left < length and arr[left] < value:
    rigth = min(length - 1, left + jump)
    if arr[left] <= value and arr[rigth] >= value:
      break
    left += jump
  if left >= length or arr[left] > value:
    return -1
  rigth = min(length-1, rigth)
  i = left
  while i < rigth and arr[i] <= value:
    if arr[i] == value:
      return i
    i +=1
  return -1

#Тестовый массив
testarr = []
for i in range (10):
  testarr.append(randint(1,50))
testarr.sort()
print(testarr)

value = int(input("Введи число: "))


# Вызов функции
if JumpSearh(testarr, value) != -1:
  print ("Элемент найден под индексом ", JumpSearh(testarr,x))
else:
  print ("Элемент отсутствует в списке")

import math
from random import randint

def JumpSearh(arr,value):
  length = len(arr)
  jump = int(math.sqrt(length))
  left = 0
  rigth = 0
  while left < length and arr[left] <= value:
    rigth = min(length - 1, left + jump)
    if arr[left] <= value and arr[rigth] >= value:
      break
    left += jump
  if left >= length or arr[left] > value:
    return -1
  rigth = min(length-1, rigth)
  i = left
  while i <= rigth and arr[i] <= value:
    if arr[i] == value:
      return i
    i +=1
  return -1

#Тестовый массив
testarr = [3, 5, 8, 13, 18, 32, 38, 38, 40, 45]
#for i in range (10):
 # testarr.append(randint(1,50))
#testarr.sort()
#print(testarr)

value = int(input("Введи число: "))


# Вызов функции
if JumpSearh(testarr, value) != -1:
  print ("Элемент найден под индексом ", JumpSearh(testarr,value))
else:
  print ("Элемент отсутствует в списке")

def InterpolationSearch(arr, value):
  low = 0
  high = (len(arr)-1)
  while low <= high and value >= arr[low] and value <= arr[high]:
    index = low + int(((float(high-low) / (arr[high] - arr[low])) * (value - arr[low])))
    if arr[index] == value:
      return index
    if arr[index] < value:
      low = index + 1
    else:
      high = index - 1
  return -1


#Тестовый массив
testarr = [3, 5, 8, 13, 18, 32, 38, 38, 40, 45]
#for i in range (10):
 # testarr.append(randint(1,50))
#testarr.sort()
#print(testarr)

value = int(input("Введи число: "))


# Вызов функции
if InterpolationSearch(testarr, value) != -1:
  print ("Элемент найден под индексом ", InterpolationSearch(testarr,value))
else:
  print ("Элемент отсутствует в списке")

def factorial_iterative(k):
    factorial = 1
    if k < 0:
        print("Нельзя вычислять факториал для отрицательных чисел")
    else:
        for i in range (1, k + 1):
            factorial = factorial*i
        print(f"Факториал числа {k} это {factorial}")
factorial_iterative(5)

def factotial_rec(k):
  if k == 1:
    return k
  else:
    return k*factotial_rec(k-1)

factotial_rec(7)

"""Тестовая папка 1"""

import os
def get_paths(path='.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))

    yield abs_path
    
    if os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)

for i in get_paths("Тестовая папка"):
  print(i)

import os
def get_paths(path='.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))
    if os.path.isfile(abs_path) is True:
      yield abs_path
    
    elif os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)

for i in get_paths("Тестовая папка"):
  print(i)