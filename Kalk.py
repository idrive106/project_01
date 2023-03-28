print ("Клавиша q завершит работу")
while True:
    s = input("Введи знак (+, -, *, /, %): ")
    if s == "q":
        break
    if s == '%':
        print('x - число от которого берём процент')
        print('y - процент который берём')
    if s in ('+', '-', '*', '/', '%'):
        try:
            x = float(input('x= '))
            y = float(input('y= '))
        except ValueError:
            print("Введите числа")
            x = float(input('x= '))
            y = float(input('y= '))
        if s == '+':
            print("%.2f" % (x + y))
        elif s == '-':
            print("%.2f" % (x - y))
        elif s == '*':
            print("%.2f" % (x * y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("Делить на 0 нельзя!")
        elif s == '%':
            print("%.2f" % (x / 100 * y))
    else:
        print("Не верный знак операции")