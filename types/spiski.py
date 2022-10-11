# list() -> (список, масив) - изменяемый последовательный тип данных который представляет из себя коллекцию каких либо объектов(значений)
# my_list = [1, 'string', False, None,[1, 2, 3]]
# print(my_list)
# print(type(my_list))

# range() - возвращает последовательность элементов (чисел)

# ls = list(range(1,101))
# print(ls)
# print(type(ls))

# ls1 = list(range(0,101,2))
# print(ls1)


# ls = list(range(1,101))
# # str1 = 'hello world'
# for num in ls:
#     # print(num ** 2 if num % 2 == 0 else num ** 3)
#     if num % 2 == 0:
#         print(f'число {num} четное квадрат: {num ** 3}')
# print(num)    
# print('finished for')

# -------------------------------------------------------------------------------
# методы списков

# print(dir([]))

# append(element) - добавляет element в конце списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(5)
# ls.append([6, 7, 8])
# ls.append(True)
# print(ls)


# extend(iterable) -> расширяет список элементами из iterable oject

# ls = [1, 2, 3]
# ls.append('hello')
# print(ls)
# ls.extend('hello')
# print(ls)

# ls = [1, 2, 3]
# ls.append([4, 5, 6])
# print(ls)
# ls.extend([4, 5, 6])
# print(ls)

# insert(<index>, <element>) - добавляет элемент по указанному index

# ls = ['string', 2, 3, False]
# ls.insert(1,4)
# ls.insert(8765, [1, 2, 3])
# print(ls)

# index(element, [start], [end]) - возвращает index элемента в списке

# ls = ['hello', 'world', 'my', 'name', 'is', 'john']
# res = (ls.index('name'))
# # res = ls.index('name')
# # print(res)
# # print(ls[res])

# print(ls[0: 2])
# print(ls[-1][0])


# # count(element) - возваращает количество вхождений elemnt в списке

# ls =[1, 2, 3, 4, 5, 6, 5, 5, 5]
# result = ls.count(5)
# print(result)

# ls = ['hello', 'world', 'my', 'name', 'is', 'john', 'north', 'king', 'queen', 'usa']
# print(ls)
# str1 = input('введите слово: ')

# if str1 in ls:
#     print(f'"{str1}" есть в списке и его индекс: {ls.index(str1)}')
# else:
#     print('net')

# sort() - сортирует список если в аргументах передать reverse=True то список будет отсортирован в убывающем порядке
# import random
# ls = []
# for x in range(0, 50):
#     ls.append(random.randint(0, 1000))

# print(ls)
# ls.sort(reverse=True)
# print()
# print(ls)

# ls = ['john', 'deyneris', 'tirion', 'Apple', 'sptw', 'scr', 'GER']
# ls.sort(key=len)
# print(ls)


# remove(element) - удаляет элемент из списка если такого нет то выводится ошибка
# pop([index]) - удаляет и возвращает элемент по индекс но если индекс не указан то удаляет последний элемент

# ls = [5, 1, 2, 4, 5, 5, 5]
# # ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)


# ls = [5, 1, 2, 4, 5, 5, 5, 99]
# deleted = ls.pop(0)
# print(ls)
# print(deleted)
# print(ls.pop())
# print(ls)


# update ----------------------------------------------------
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)











