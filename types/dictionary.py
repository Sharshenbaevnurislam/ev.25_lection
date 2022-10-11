# dict() - словарь -> упорядочное колекция элементов (python 3.7 -> ordered) каждый элемент в словаре хранится в виде пары: {ключ: значение}

# ассоциативный масив hash tables, object(js), structer == dictiotionali(py) 

# ключами могут выступать только неизменяемые типы данных и в словарях хранится уникальные ключи тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }
# print(thisdict)
# print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])


# a = dict()
# b = {}
# c = set()
# print(a,b)
# print(type(a))
# print(type(b))
# print(type(c))

# ls = [('key1', 'value1'), ('key2', 'value2')]
# dict_ = dict(ls)
# print(dict_)

# --------------------------------------------------------------

# print(dir(dict))

# items, keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',
# }
# print(user_info.items())
# print()
# print(user_info.keys())
# print()
# print(user_info.values())

# for value in user_info.values():
    # print(value)

# print(user_info)
# for key, value in user_info.items():
#     print(f'key: {key}, value: {value}')

# a = list(user_info.items())
# print(a[0])


# изменение элементов в словаре

# dict_ = {'name': 'Jack', 'age': 24}

# # print(dict_ ['name'])
# # dict_['name'] = 'John'
# # dict_['address'] = 'WinterFell'
# # print(dict_)

# dict_.update({'name': 'John', 'address': 'WinterFell'})
# print(dict_)

# --------------------------------------------------------------------------------
# # создание - fromkeys
# dict_ = {}
# ls = list(range(1,101))
# new_dict = dict_.fromkeys(ls, 'value')
# print(new_dict)

# --------------------------------------------------------------------------------
# get
# dict_ = {1: 'pizza', 2: 'burger', 3: 'steak'}
# print(dict_.get(2))
# print(dict_[2])

# setdefault - работает также как и get но если нет такого  ключа то создает новую пару занчения из этого ключа


# dict_ = {'name': 'eddard', 'last_name': 'stark', 'age': 28}
# print(dict_)
# print(dict_.setdefault('age',38))
# print(dict_)


# удаление элементов 
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dict_ = {'name': 'john', 'last_name': 'snow'}

# removed = dict_.pop('address', 'такого ключа нет ')
# print(dict_)
# print(removed)


# popirem() - удаляет последнию пару

# dict_ = {'name': 'john', 'last_name': 'snow'}
# removed = dict_.popitem()
# print(dict_)
# print(removed)





























