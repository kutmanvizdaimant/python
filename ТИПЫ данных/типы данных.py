#                        set - множество

# add =
# remove =
# copy =
# discard =
# clear =
# difference = кесилуушу
# symmetric_difference = (^) = жаны переменада айырмасы
# issubset =
# issuperset =
# frozenset = озгоргонго зашита

# a = input()
# b = list(a)
# print(set(b))
#                          len = узундугу
# user = {'mike', 'bill', 'ted'}
# print(len(user))
#                           add == как append кошуп коебуз
# user = set()
# user.add('sam')
# user.add('chynara')
#                     remove == удаление элемента  discard = удаление без элемента
# user = {'mike', "tom", 'bill', 'ted'}
# users = 'tom'
# if users in user:
#     user.remove(users)
# print(user)
#                          copy =
# name = user.copy()
# print(name)
#                          union = объединение множество
# user = {'tim', 'tom', 'alisa'}
# users = {'tim', 'kutman', 'islam'}
# union = user.union(users)
# print(union)
#                          intersection == пересечение (окшош сандары)
# найдите пересечение множеств а и б
# A = {1, 2, 3, 4, 5}
# B = {3, 4, 5, 6, 7}
# C = A.intersection(B)
# print(C)
#                         intersection_update = обнавляет пресеченными элемента
# user = {'tim', 'tom', 'alisa'}
# users = {'tim', 'kutman', 'islam'}
# user.intersection_update(users)
# print(user)
#                       difference = разность множество
# user = {'tim', 'tom', 'alisa'}
# users = {'tim', 'kutman', 'islam'}
# diferense = user.difference(users)
# print(diferense)
#                        symmetric_difference (^)= оъединение без пересечение
# user = {'tim', 'tom', 'alisa'}
# users = {'tim', 'kutman', 'islam'}
# union = user.symmetric_difference(users)
# print(union)
# users1 = user ^ users
# print(users1)
#                         issubset = подмножество выясняеть
#                         issuperset = наоборот
# a = {'alisa', 'kutman', 'tim'}
# b = {'alisa', 'kutman', 'tim', 'islam', 'bob'}
# print(a.issubset(b))
# print(b.issubset(a))
#
# a = input("введите список:")
# b = input("повторите")
# set1 = set(a)
# set2 = set(b)
# uniq = set1.intersection(set2)
# print(uniq)

# a = input()
# b = a.split()
# c = list(set(b))
# print(c)


# a = input("введите список:")
# b = input("повторите")
# user = set(a)
# users = set(b)
# c = user.symmetric_difference(users)
# print(c)

# a = input()
# b = a.split()
# c = list(set(b))
# t = []
# for i in c:
#     t.append(int(i) ** 2)
# print(t)
#                 Tupple ==  картеж не изменяемый

# срезы =

# name = ("kutman", 23)
# print(type(name))

# name = "kutman", 23, "agahan"
# print(name)

# name = ("kutman",)
# print(type(name))

# date = ["islam", 29, "google",]
# name = tuple(date)
# print(len(name))
# обращение к элементам картежа
# print(name[0])
# print(name[1])
# print(name[-1])

# name, age, company, position = ('syimyk', 27, 'google', 'software developer')
# print(name)
# print(age)
# print(company)
# print(position)

# name = ('syimyk', 27, 'google', 'software developer')
# a = name[0:3]
# print(a)

# name = ('syimyk', 27, 'google', 'software developer')
# for item in name:
#     print(item)

# name = ('syimyk', 27, 'google', 'software developer')
# i = 0
# while i < len(name):
#     print(name[i])
#     i += 1

# name = ('Syimyk', 27, 'google', 'software developer')
# first_name = 'Syimyk'
# if first_name in name:
#     print('пользователь зовут том')
# else:
#     print("другое имя")

# name = ('syimyk', 27, 'google', 'software developer', 'Syimyk' )
# print(name.index('Syimyk', 1))