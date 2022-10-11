# sentence = input('введите предложение:')

# if sentence[-1] == '?':
#     print('предложение вопросительное')
# else:
# #     print('обычное предложение')

# sentence = input('введите предложение:')
# print('предложение вопросительное' if sentence[-1] == '?' else 'Обычное предложение')
#---------------------------------------------------------------------------------------------
# ternary operator(тернарный оператор) - конструкция которая аналогично по своим свойствам  и действию конструкции if/else, при этом записывается в одну стройчку кода

# <выражение если в условии True> if <условия> else <выражение если False>

# number = 18
# res = 'even' if number % 2 == 0 else 'odd number'
# # print (res)


# from string import digits

# symbols = digits + '-'
# print(symbols)
# number = input('введите число: ')
# is_correct = True
# for i in number: #567
#     if i not in symbols:  #0123456789-
#         is_correct = False
# if is_correct:
#     print('Yes number')
#     number = int(number)
#     print('your number:', number)
#     result = number if number >= 0 else -number 
#                                             #-(-56)
#     print(result)                                      
# else:
#     print('invalid values') 





# if number.isdigit():
#     number = int(number)
#     print('да число')

# else:
#     print('вы велли не число')
#----------------------------------------------------------------------------------------------

from string import digits

flag = True
symbols = digits + '-' + '.'

while flag:
    # choice = input('введите yes or not: ')
    # if choice == 'not':
    #     flag = False
    is_correct_number = True
    num1 = input('введите первое число: ')
    num2 = input('введите второе число: ')
    if len(num2) <= 1 and (num2 == '.' or num2 == '-') or not num2:
        print('вы ввели не правильное число')
        is_correct_number = False
    for x in num2:
        if x not in symbols:
            print('вы ввели не правильное число')
            is_correct_number = False
            break
    if len(num1) <= 1 and (num1 == '.' or num1 == '-') or not num1:
        print('вы ввели не правильное число')
        is_correct_number = False
    for x in num1:
        if x not in symbols:
            print('вы ввели не правильное число')
            is_correct_number = False
            break
    if not is_correct_number:
        continue
    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    operator = input('введите оператор(+, -, /, *): ')
    if operator == '+': 
         print(f'результат: {num1 + num2}')
    elif operator == '-':
        print(f'результат: {num1 - num2}')
    elif operator == '*':
        print(f'результат: {num1 * num2}')
    elif operator == '/':
        if num2 == 0:
            print('на ноль делить нельзя')
        else:
            print(f'результат: {num1 / num2}')
    else:
        print('вы ввели не правильный оператор')
    choice = input('хотите остановить(yes): ')
    if choice.lower() == 'yes':
        flag = False
        print('пока')
    































































