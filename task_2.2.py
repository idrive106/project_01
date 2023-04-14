# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    elif month >= 10 and month <= 12:
        return 4
    else:
        return None

months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

while True:
    month_str = input("Введите номер месяца (1-12): ")
    try:
        month = int(month_str)
        if month < 1 or month > 12:
            raise ValueError
    except ValueError:
        print("Ошибка: введите число в диапазоне от 1 до 12")
        continue
    else:
        break

quarter = quarter_of(month)
month_name = months[month - 1]

if quarter is not None:
    print(f"{month_name} является частью {quarter}-го квартала")
else:
    print("Некорректный номер месяца")