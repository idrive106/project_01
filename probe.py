# Задача 1
# Приведем список покупок в магазине
 
shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

shop_list.insert(2,'Рыба')
# либо shop_list.index('Рис'),
print(shop_list)

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди
 
#   а. Вставьте рыбу между горошком и рисом
 
#print(type(shop_list), len(shop_list))
 
#   b. Добавьте фрукты из списка fruits в конец списка shop_list
 
fruits = ['Яблоко', 'Апельсин', 'Клубника']

shop_list.extend(fruits)
print(shop_list)
 
#   c. Удалите из списка shop_list картофель (pop или remove)

shop_list.pop(0) # либо shop_list.pop(shop_list.index('Картофель'))
print(shop_list)

#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
print(shop_list.index('Хлеб'), shop_list.index('Апельсин'), sep='\n')

#   Номер "продукта" в списке - N

# Функции print(), type(), len() у функций функция указывается перед скобками, а в скобках переменная.
# Метод указывается через точку например переменная.метод()
# Как узнать какие методы у конкретного типа данных?
#from pprint import pprint
 
#pprint(dir(name))