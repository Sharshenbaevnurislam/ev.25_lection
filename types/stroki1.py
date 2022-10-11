# string - строки

# 'hello world'
# "hello world"
# '''
# hello world
# '''

# a = 5 # - комент

# строки - это набор последевотельных символов которые мы используем для хранение и представления текстовай информации. набор методов и операций которые мы можем 
# использовать с данными в виде текста

# инедексация в строке 
# name = 'john'
        # J = 0 = -4
        # o = 1 = -3
        # h = 2 = -2
        # n = 3 = -1
# print (name)
# print(name[1])
# print(name[-1])

# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print (str1[-3], str1[-2], str1[-1])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])


# срезы по индексам
# [start: end: <step]
# str1 = 'birthday'
# str2 = str1[0:5]
# print(str2)
# print(str1[5:25])
# print(len(str1))
# print(str1[5:]) #до конца
# print(str1[:5])

# text = 'hello world my name is john \''
# print(len(text))
# print(text)

# print(text[:12])
# print(text[13: 19])
# print(text[20:])
# print(text[:12:3])
# print(text[::2])
# print(text[:: -1])
# print(text[:12:-1])


# конкатенация строк(слияне, соеденение)

# word1 = 'hello'
# word2 = ' world'
# probel = ''

# result = word1 + probel + word2
# print(result)
# print(word1 + probel + word2 + '!')


# цформатирование строк
# 1. с помощью знака %
# 2. с помощью (.format())
# 3. интерполяция строк (f-строки)

# # %
# name = input('enter your name:')
# last_name = input('enter your last name:')
# print('hello, my name  is ', name, last_name)
# print('hello, my name  is' + ' ' + name + ' ' + last_name)
# print('hello, my name is %s %s' %(name, last_name))

# .format
# name = input('enter your name:')
# last_name = input('enter your last name:')
# print('hello, my name is {} {}'.format(name,last_name))

# # f - строки
# name = input('enter your name:')
# last_name = input('enter your last name:')
# print(f'hello, my name is {name} -> {last_name}')


# экранирование строк -  механизм при помощи которго можно вставлять символы, которые сложно ввести с клавиатуры в строк
#   \n - перенос строки
# \t - горизонтальная табуляция
# \v - вертикальная табуляция

# name = 'John\ \nSnow'
# lastName = '\vSnow'
# last_name = '\tSnow'

# print(name)
# print(lastName)
# print(last_name)






















































































