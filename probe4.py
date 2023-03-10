# Операторы цикла 
# while
 
# Последоватиельность Фибоначчи
# №       1 2 3 4 5 6 7 ... 100
# Число   1 1 2 3 5 8 13 ... ?
 
fib1, fib2 = 1, 1
 
search = input('Введите искомый номер последовательности: ')
i = int(search) - 2
 
while i > 0:
    print(fib2)
    fib1, fib2 = fib2, fib1 + fib2 
    # print(f'Счетчик {i}')
    i -= 1
 
print(fib2)

# Словарь хранит ключ значение
capitals = {}
capitals['Россия'] = 'Москва'
capitals['Италия'] = 'Рим'
 
print(capitals)

# Операторы цикла 
# for
 
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
 
# Через while
# i = 0
# while i < len(room_prices):
#     print(room_prices[i])
#     i += 1
 
# через for
for price in room_prices:
    print(price)
 
# for ind in range(len(room_prices)):
#     print(room_prices[ind])
 
# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год ... отнять )
 
employees = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121
    }
 
# Вариант 1
top_managers = []
for name in employees.keys():
    if employees[name] >= 100000:
        top_managers.append(name)
 
print(top_managers)
 
# Вариант 2
top_managers = [name for name, salary in employees.items() if salary >= 100000]
 
print(top_managers)