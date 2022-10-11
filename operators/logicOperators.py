# операторы сравнение
# условные операторы
# логические операторы

# операторы сравнения
# <, >, ==(равно), <=, >=, !=(не равно)


# 1 < 5 -> true
# 7 > 9 -> false
# num1 = 15
# num2 = 15
# print(num1 != num2)


# num1 = 20
# num2 = 17
# print(num1 >= num2)


# stroka1 = 'Hello'
# stroka2 = 'World'
# print(stroka1 > stroka2)
        #  72    #87

# print(ord(' '))
# print(ord('а'))

# print(chr(1080))

# stroka1 = 'Hello!'
# stroka2 = 'World John snow'
# print(len(stroka1)  > len(stroka2))


# условные операторы
# if
# elif
# else

# if <connection>: 
#     <body if> #сработает если выражении if придет true
# [elif]:
#     <body else> срабатывает если во всех выше стоящих условиях false


# string = input('enter smt: ')

# if string.lower() == 'hello':
#    print('hello stranger')
# elif string.lower() == 'john':
#     print('welcome john')
# elif string.lower() == 'abra-kadabra':    
#     print('sim salamon ')
# else:
#     print('net')
# print(string)


# email = input('enter email: ')
# password1 = input('enter the password: ')

# if len(password1) < 8:
#   raise ValueError('password too short')

# password2 = input('enter the password confirmation')  

# if password2 != password1:
#   raise ValueError('password didn\' match')
# else:
#   print('successfuly signed up')


# age = input('enter you age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('говно переделывай')

# if age < 18:
#     print(f'маленький еще приходи через {18 - age} годиков')

# else:
#     print('ладно уговорил')


# логические операторы 
# and -> логическое и 
# or -> лог или
# not -> лог отрицание

# my_age = 20
# your_age = 18
# result = my_age == 20 and your_age == 19
# print(result)

# result = my_age == 21 or your_age == 19
# print(result)

# result = not my_age == 20
# print(result)


# user = 'john'
# is_google_user = True
# is_github_user = True
# is_age_greater_21 = False
# user_coins = 9000
# # либо юзер гугла или гитхаба и либо возраст выше 21 либо деньги(8000)
# if (is_google_user or is_github_user) and (is_age_greater_21 or user_coins > 8000):
#   print(f'you can enter the system Mr/Mrs {user}!')
# else:
#         print('sorry, you couldn\'t enter')


# оператор индефикации
# in ->проверяет наличие элемента внутри кого либо интерисуемого объекта(строки спики и т д)
# is-> сравнивает ячейки памяти двух объектов 
#   == -> сравнивает по значению
# is not -> отрицательлнок сравнивание ячеек памяти

# str1 = 'hello world'
# print(str1)
# choice = input('enter the symbol: ')

# if choice in str1:
#         print(f'the symbol: {choice} exits')
# else:
#         print(f'the symbol: {choice} does not exits')

































