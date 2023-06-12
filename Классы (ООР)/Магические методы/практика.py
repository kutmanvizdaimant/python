# class Lst:
#     def __init__(self, name, lst):
#         self.name = name
#         self.lst = list(lst)
#
#     def __add__(self, other):
#         if not isinstance(other, Lst):
#             raise ValueError('aflsisbbd')
#
#         return self.get_sum(self.lst) + self.get_sum(other.lst)
#     def get_sum(self, lst):
#         a = 0
#         for i in lst:
#             if i % 2 == 0:
#                 a += i
#         return a
# a1 = Lst('Student', [4, 5, 4, 5, 4, 3])
# a2 = Lst('car', [2503, 2400, 1343, 1500])
# print(a1 + a2)


# class Car:
#     def __init__(self, name, prices):
#         self.name = name
#         self.prices = list(prices)
#     def get_sum(self, prices):
#         a = 0
#         for i in prices:
#             if i > 1500:
#                 a += i
#         return a
#     def __eq__(self, other):
#         if not isinstance(other, Car):
#             raise ValueError('kutman')
#         return self.get_sum(self.prices) == self.get_sum(other.prices)
# a1 = Car('bmw', [2435, 600, 1500, 4500])
# a2 = Car('mersedes', [1500, 4500, 2435, 1200])
# print(a1 == a2)

# class Name:
#     def __init__(self, names):
#         self.names = names
#     def __mul__(self, other):
#         if not isinstance(other, Name):
#             raise ValueError("kutman")
#         return self.get_walue(self.names) * self.get_walue(other.names)
#     def get_walue(self, names):
#         max = 0
#         for i in names:
#             if max < len(i):
#                 max = len(i)
#         return max
# a1 = Name(['Ainazik', 'agahan', 'kutman'])
# a2 = Name(['Nursultan', 'isam', 'roma'])
# print(a1*a2)
