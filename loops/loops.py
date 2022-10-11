# циклы -  это конструкция при помощи которых можно организовать многократное исполнение определенного кода

# while <expression>:
#         <body>
# <else>:
# #         <body>

# i = 1
# while i <= 10:
#     print('цикл выполниля {i} раз')
#     i += 1 
# else: 
#     print('конец цикла')

# # print('начало кода')


# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('Введите имя: ')
#     name = input('Введите имя 2: ')
#     i += 1
#     if i >4:
#         print('цикл остановлен')
#         break
# else:
#     print('вы ввели правилное имя')


# admin = 'johnsnow23', 'ilovepython23'
# i = 3

# username = None
# password = None

# while username != admin[0] or password != admin[1]:
#     username = input('введите username: ')
#     password = input('введите password: ')
#     i -= 1
#     if i == 0:
#         print('вы заблокированы на 5 минут')
#         break
# else:
#     print(f'{admin[0]} вы успешно зашли в систему')

# --------------------------------------------------------------------------------------------------

# for <variable> in <iterable object>:
    #  <body

# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for x in list_:
#     print(x)


# ____________________________________________________________________________________________________________________


# ls =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# # for x in ls: 
# #     print(f'element: {x}')

# i = 0
# while i < len(ls):
#     print(f'element: {ls[i]}')
#     i += 1


# ------------------------------------------------------------------------------------------------------------------------

# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('введите секретный код: ')

# while word not in secret_list:
#     print('Incorect word! try one more time')
#     word = input('введите секретный код: ')

# print('You\'re welcome my friend, {word}!')


# --------------------------------------------------------------------------------------------------------------------------

# steps = 8
# path = "UDDDUDUU"
# res = 1

# # 2)
# steps = 9
# path = 'UDDUUDDUU'
# res = 2
# # sea_level = 0

# steps = 9
# path = 'UDDUUDDUU'
# sea_level = 0
# dolina = 0
# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     elif x == "D":
#         sea_level -= 1

# print(dolina)










