#                        1 задания наследование

# class Shape:
#     def get_pr(self):
#         pass
#
# class Treangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def get_pr(self):
#         return self.c + self.b + self.a
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def get_pr(self):
#         return 2 * (self.a + self.b)
#
# class Square(Shape):
#     def __init__(self, a):
#         self.a = a
#     def get_pr(self):
#         return 4 * self.a
# tr = Treangle(4, 5, 6)
# re= Rectangle(2, 3)
# sq = Square(6)
# shape_angle = [tr, re, sq]
# for i in shape_angle:
#     print(i.get_pr())
#
# # 1 задания  инкапсулясия
#
#
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def deposit_balance(self, balance):
#         self.__balance += balance
#
#     def whithdraw_balance(self, balance):
#         if self.__balance >= balance:
#             self.__balance -= balance
#         else:
#             raise ValueError("kjhf;wiv")
#
#     def get_info(self):
#         print(f" на вашем счете: {self.__balance}")
#
# a = BankAccount(50)
# a.deposit_balance(100)
# a.whithdraw_balance(50)
# a.get_info()
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         print(f"name: {self.name} age: {self.age}")
#
# class Student(Person):
#     def __init__(self, name, age, university):
#         super().__init__(name, age)
#         self.university = university
#     def get_info(self):
#         print(f"name: {self.name} age: {self.age} university: {self.university}")
#
# class Teacher(Person):
#     def __init__(self, name, age, salery):
#         super().__init__(name, age)
#         self.salary= salery
#
#     def get_info(self):
#         print(f"name: {self.name} age: {self.age} salary: {self.salary}")
#
#
# c = Person("kutman", 18)
# c.get_info()
# a = Student("agahan", 19, "niobis")
# a.get_info()
# b = Teacher("aidai", 20, 250000)
# b.get_info()

# class Matrix:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.lst):
#             return self.lst[item]
#         else:
#             raise IndexError('неверный индекс')
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('индекс должен быть целым он сан')
#     def __delitem__(self, key):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('индекс должен быть целым он сан')
# a1 = Matrix([[1, 2, 3, 4],[5, 6, 7, 8]])
# print(a1[0][0])
# a1[0][0] = 15
# print(a1.lst)
# del a1[0][0]
# print(a1.lst)


def sum(lst):
    a = 0
    for i in lst:
        if i % 2 == 0:
            a += i
    print(i)
lst = [24, 2, 3]