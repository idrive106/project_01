# Принцип DRY - Dont repeat yourself
# Создание функции
# def greeting(name):
#     print(f'Hello, {name}')
 
# # Вызов функции
# greeting('Mark')
 
# # Вызов функции с параметром
# for i in ['Mark', 'R2D2', 'Anakin', 'World']:
#     greeting(i)

# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год ... отнять )
 
# Структура файла с кодом
# 1 Импорты 
# import чото
 
# 2 функции
# def чото():
#     print(чото)
 
# 3 код который содержит цикл или инициализацию
 
print('Start Debuging')
 
def get_topmgrs_list(dct_report):
    mgrs_list = []
    for name in dct_report.keys():
        if dct_report[name] >= 100000:
            mgrs_list.append(name)
    return mgrs_list
 
employees = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121
    }
 
top_managers = get_topmgrs_list(employees)
print(top_managers)