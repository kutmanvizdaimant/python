#                             def имя_функция
#                             параметры
#                            после * = именнованный
# / = позиционный

# def find_max_element(list):
#     print(max(list))
# a = [1, 2, 3, 4, 5, 100, 23]
# find_max_element(a)

# def find_index(lst, number):
#     a = lst.index(number)
#     print(a)
# find_index(a, 5)

# def print_name(name):
#     pass
# print_name(a+b)

# def print_name(name):
#     if name == 'Agahan':
#         print(name)
#     else:
#         print('другое имя')
# print_name('Agahan')
# print_name('kutman')

# def find_sum_int(string):
#     a = 0
#     for i in string:
#         if i.isnumeric():
#             a += int(i)
#     print(a)
# find_sum_int('asdfasd1234567')

# def find_sum(lst, number=0):
#     a = 0
#     for i in lst:
#         if number == 1 and i % 2 == 1:
#             a += i
#         elif number == 0 and i % 2 == 0:
#             a += i
#     print(a)
# find_sum([1, 2, 3, 4, 5, 6, 8, 10])

# def find_sum_index(lst, number1, number2):
#     a = lst.index(number1)
#     b = lst.index(number2)
#     print(a+b)
# find_sum_index([1, 2, 3, 4, 5, 6, 8, 10], 4, 5)

# def diff(lst1, lst2):
#     a = 0
#     b = 0
#     for i in lst1:
#         a += i
#     for i in lst2:
#         b += i
#     print(a - b)
# diff([1, 2, 3, 4, 45, 100], [1, 2, 3, 4, 5, 13, 7, 13])

# def find_number(number):
#     if number % 2 == 0:
#         print(True)
#     else:
#         print(False)
# find_number(18)
# find_number(21)

# def sum(lst):
#     b = 0
#     for i in lst:
#         b += i
#     print(b)
# sum([1, 2, 3, 5, 5])

# a = [1, 2, 3, 5, 5]
# def find_avg(lst):
#     b = sum(lst)/len(lst)
#     print(b)
# find_avg(a)
# find_avg([3, 5, 5, 6, 8, 9])

# a = [3, 5, 5, 6, 8, 9]
# def find_number(lst):
#     for i in lst:
#         if i % 2 == 0:
#             print(i, end='  ')
# find_number(a)

# a = [1, 2, 3, 4, 5, 6, 99]
# def find_square(lst):
#     for i in lst:
#         b = i ** 2
#         print(b)
# find_square(a)

# b = [1, 2, 1, 2, 5, 3, 4, 1, 2]
# def find_unique(lst):
#     print(list(set(lst)))
# find_unique(b)
# find_unique(b)

# def find_avg(lst):
#     return (sum(lst)//len(lst))
# t = find_avg([1, 2, 3, 4, 5, 6, 7, 8])
# print(t)
# c = 3 * t
# print(c)

# a = [1, 3, 4, 12, 14, 15, 18, 20, 39]
# def find_sum(lst):
#     b = 0
#     for i in lst:
#         if i % 2 == 1:
#             b += i
#     return b
# t = find_sum(a)
# c = 0
# for i in a:
#     if i % 2 == 0:
#         c += i
# print(t-c)
