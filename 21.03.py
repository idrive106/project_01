# 1

salary = float(input('Введите зарплату '))
expenses = float(input('Введите расходы '))
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tempexp = expenses
tempsal = salary
if salary <= expenses:
    print('Поданы не правильные данные в программу')
else:
    for i in months:
        print('Сейчас месяц ', i)
        if i != 1:
            salary = salary * 1.05
            tempsal = tempsal + salary
            print('Зарплата:', tempsal)
            tempexp = expenses * i
            print('Расходы: ', tempexp)
        else:
            print('Первый месяц без процентов')
            print(salary, expenses)
live = abs(tempsal - tempexp)
print ('Сотрудник накопит', round(live,2), 'рублей')


# 2

arr = [-3, 2, 4, 0, 5]
k = 9
result = []

for x in arr:
    for y in arr:
       if x + y == k:
        result.append([x, y])
print(result)


# еще один способ не работает!!!

# arr = [-3, 2, 4, 0, 5]
# k = 5
# result = []
# low = 0
# high = len(arr)-1

# while low < high:
#     sum = arr[low] + arr[high]
#     if sum == k:
#         result.append([arr[low], arr[high]])
#     if sum < k:
#         low += 1
#     else:
#         high -= 1
# print(result)



