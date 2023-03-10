# Циклы

# Условный оператор if, elif, else

# Заданы размеры коробки box_x, box_y и товара product_x, product_y
# Определить, поместится ли товар в коробке (габариты товара параллельны размеру коробки)
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if (если)/elif(иначе если)/else(иначе), можно вложенные
box_x, box_y = 10, 7
product_x, product_y = 8, 9
 
# проверить для
# product_x, product_y = 9, 8
# product_x, product_y = 8, 6
# product_x, product_y = 3, 4
# product_x, product_y = 11, 9
# product_x, product_y = 9, 11
 
# Раскомментируйте нужную строку

# Вариант 1
if box_x >= product_x:
    # print('По грани x входит')
    if box_y >= product_y:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')
 
# Вариант 2
if box_x >= product_x and box_y >= product_y:
    print('Да')
else:
    print('Нет')
 
# Вариант 3
print(True if box_x >= product_x and box_y >= product_y else False)