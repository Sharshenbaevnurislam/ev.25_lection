
prodolzhit = 'y'
while prodolzhit == 'y':
    num1 = float(input('Введите первое число:'))
    oper = input('Введите операцию:')
    num2 = float(input('Введите второе число:')) 
    if oper == '+':
     print(num1 + num2)
    elif oper == '-':
      print(num1 - num2)
    elif oper == '*':
       print(num1 * num2)
    elif oper =='/':
       print(num1 / num2)
    else:
       print('Error')
    prodolzhit = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить: ")










    