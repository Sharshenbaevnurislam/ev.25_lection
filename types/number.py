# Типы данных -> Числа int(), float()


# number = 5  #varible (переменная)
# print (number)
# number = 51
# print (number)
# # = -> оператор присваиваиния 

# tommorow_day -> snake case 
# tomorowDay -> Camel case 
# abc -> нижний регистр
# ABC -> верхний регистр

# # + 
# a = 5
# b = 15
# result = a + b 
# print (result) 

# # print('Результат примера 5 и 15'5 + 15)

# a =  100 
# b =  1000
# c = 500 #int
# # d = 56.25 #float
# print(a + b + c + d)

# # -
# # num1 = 996
# # num2 = 67.55
# print(num1 + num2)

# # *
# num1 = iny(input('ведите число 1:'))
# num2 = int(input(ведите число 2 :))
# result = num1 * num2
# print ('результат')
# num1, 'и', num2, 
# 
# num = '15'
# num = int(num)
# print(type(num))


# # / and // and %
# / -> обычное деление
# // -> целочисленное деление (деление без остатка)
# % -> модульное деление (остаток от деления)

# num1 = 5
# num2 = 2
# print (num1 / num2)
# print (num1 // num2)
# print (num1 % num2)

# ** -> возведение в степень

# num1 = 5
# print(num1 ** 1000)



# pow(a,b,<mod>) -> функия возведения числа а в степень 
# print(pow(2,5,5)) # 2 ** 5 % 5 -> 2



#  divmod (a,b) -> она выводит два числаб первое число это результат целочисленного деления (//), а второе число это модульное деление (%) дыух чисел
# res = divmod(32,5)
# print (res)


# round() -> функция округления числа
# res = 24 / 13
# print (round(res, 1))

# abs() - абсолютное значение -> abs (5-) = 5 -> (-5) = 5


# print(abs(-101))
# print(abs(50))


# import math
# from math import pi, sqrt

# print(pi)
# print(sqrt(25))


# print(math.pi)
# math.sqrt -> корень числа

# print(math.sqrt(25))
# print(math.sqrt(101))
# print(math.sqrt(6))


# dir() - возвращает меоды обьекта или функции определенного модуля 

# import math

# print(dir(math))


# ''' Множественное присваивание'''

# a = 5
# a,b,c = 1,2,3
# v = 5
# n=7
# d = 3
# v,n,d = d,v,n 
# print(v,n,d)


'''
1. даны две переманый num1 со значением 10 и num2 со значением 3.
Поменяйте значение этих переменый между собой. Важно: нельзя использовать множественное присвавинае

'''

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print (num1, num2)


# print('hello' * 3) #дублирование строк


# str1 = '12'
# num1 = 2
# print(str1+str(num1))


'''
инкремент и дикремент
'''

# инкремент - увеличение значение какой либо переменной. пример: (a = 1 a += 1 -> a = a +1)
# a = 11
# a += 1
# print (a)


# дикремент - уменьшение значения какой либо переменной. (a -= 1 -> a = a - 1)

# a = 0 
# a -= 1
# print(a)


# *
# a = 5
# a *= a
# print (a)

# a = 10 
# a /= 2 
# print(a)

# a = 7 
# a %= 2
# print (a)


# id() -  номер в ячейке памяти
# если числа или слова разные то айди будет другим
# a = 1
# b = 1
# print(id(a))
# print(id(b))


# type() -> выводит тип заданное переменной
# a = 9
# b = 'hello'
# print(type(a))
# print9type(b)


# var = int(input('ведите число'))


'''
примем от пользователя два значенияб переведем в тип данных int и возведем первое число в степень второго числа
# '''
# num1 = int(input('введите число:'))
# num2 = int(input('введите степень:'))
# print(num1 ** num2)


'''
модуль random - предоставляет функции для генерации случайных чисел букв и символов
'''
# import random

# # print (dir(random))

# num = random.randint(11111, 99999)
# print(num)


from random import choice 
import string
print (string.ascii_letters)
a = choice(string.ascii_letters)
print(a)

'''
дана переменная с радиусом окружностиб найдите периметр и площадь окружностиб результат выведите в терминале
'''
# периметр 2 * r * pi
# площадь pi *(r ** 2 )

from math import pi
r = int (input('введите радиус'))
result_P = 2 * r * pi
result_S = pi * (r ** 2)
print('площадь окружности', round(result_S))
print('периметр окружности', round(result_P))













































