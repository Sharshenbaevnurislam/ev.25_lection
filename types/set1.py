# {} !!!
# a = {1: 'a'} словарь
# a = {1,2,3} множества

# set_ = {8,1,2,3,4,5,6,7,7,7,7,7}
# print(set_)
# print(type(set_))

# ls = [1,2,'a',0, False, True, 'n']
# str1 = 'My name is John Snow'
# # ls.extend(str1)
# print(ls)
# res = list(set(ls))
# print(res)

# print(ls)
# set1 = {*ls}
# res = [*set1]
# print(set1)
# print(type(set1))
# print(res)
# print(type(res))

# FIFO / LIFO
# a = {1,2,3,4,5}
# print(a)
# a.pop()
# print(a)

# remove -> error
# discard -> None
# set_ = {1,2,3,4,5,6,7}
# print(set_.discard(5))
# set_.remove(8)
# print(set_)

# frozenset
# a = {1,2,3,4,5}
# f_set = frozenset([1,2,3,4,5])
# print(type(a))
# print(type(f_set))
# print(a)
# print(f_set)
# print(dir(f_set))

# a = set('qwerty')
# b = frozenset('qwerty')
# a.add(1)
# print(a)
# b.add(1)
# print(b)







# Составьте код которая принимает номер месяца вашего рождения и в зависимости от сезона печатает на выходе следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>».

# В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона: 
# - для зимы «За окном падал белый снег»,
# - для весны «Птицы пели прекрасные песни»,
# - для лета «Солнце светило ярче чем когда-либо»,
# - для осени «Урожай был невероятным».

# Важно учесть, что пользователи могут ввести любой тип данных в качестве аргумента (не попадитесь на этом и предупредите о том, что 
# «Требуется ввести реальный номер месяца»).


months = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7:'july',
    8: 'august',
    9: 'september',
    10: 'octomber',
    11: 'november',
    12: 'december'
}

while True:
    number = input('введите номер месяца: ')
    if number == 'john':
        break

    if not number.isdigit():
        print('требуется ввести реальный ')
        continue
    number = int(number)
    if number not in range(1,13):
        print('требуется ввести реальный ')

    if number in range(3,6):
        print(f'вы родились в {months[number]}. Птицы пели прекрасные песнию')
    elif number in range(6,9):
        print(f'вы родились в {months[number]}. Солнце светило ярче чем когда-либо')
    elif number in range(9,12):
        print(f'вы родились в {months[number]}. Урожай был невероятным')
    else:
        print(f'вы родились в {months[number]}. За окном падал белый снег')











