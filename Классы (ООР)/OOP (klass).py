# class Person: # Атрибуттары
#     age = 18
#     eye = "kare"
#     hair = "kuron"
#     height = 175
#
# a = Person()
#
# print(a.age)
# print(Person.__dict__)
# print(getattr(Person, "height"))
import asyncio

# a.hair = "кыпкызыл"
# b = Person()
# print(a.hair)
# print(b.hair)  # isinstance
# print(isinstance(a, int))
# a.strength = 20
# setattr(b, "scin", "black")
# del Person.hair

# class Cat:
#     age = 8
#     breed = "persian"
#     height= 20
#     weight = 6
#     def miyu(self):
#         print("my name is jony")
# a = Cat()
# a.breed = "siamese"
# setattr(a, "skin", "white")
# b = Cat()
# del Cat.age
# print(Cat.__dict__)
# print(a.__dict__)
# print(b.__dict__)

# class Home:
#     type = "pivate"
#     square = 4.5
#     address = "sokuluk"
#     color = "white"
#     def get_info(self):
#         print(f"type {self.type} {self.square} {self.address} {self.color}")
# a = Home()
# a.get_info()

# частный квартира
# сотик
# адрес
# цвет

# class Cat:
#     def __init__(self, breed, age, color):
#         self.breed = breed
#         self.color = color
#         self.age = age
#
#
# a = Cat('siam', 12, 'white')
# print(a.breed, a.color, a.age)

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average_grades(self):
#         return sum(self.grades)//len(self.grades)
#
#
# a1 = Student("Kutman", [4, 4, 5, 3, 5, 5])
# a1.average_grades()

# class Student:
#     def __init__(self, first_name, last_name, groups, grades):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.groups = groups
#         self.grades = grades
#
#     def average_grades(self):
#         # print(sum(self.grades)//len(self.grades))
#         return sum(self.grades)//len(self.grades)
#
#     def get_info(self):
#         if self.average_grades() == 3:
#             print("плохо")
#         elif self.average_grades() == 4:
#             print("хорошо")
#         elif self.average_grades() == 5:
#             print("отлично")
#
#
# a1 = Student('kutman', "zamirbek", "mpd", [5, 5, 4, 3, 4, 5, 2, 4, 5])
# print(a1.average_grades())
# a1.get_info()

# class BankAccount:
#     def __init__(self, number, balance):
#         self.account_number = number
#         self.balance = balance
#     def add_balance(self, balance):
#         self.balance += balance
#     def minus_balance(self, balance):
#         if self.balance >= balance:
#             self.balance -= balance
#         else:
#             print("недостаточно средств")
#
#     def get_info(self):
#         print(self.balance)
# a = BankAccount("Agahan", 1000)
# a.add_balance(500)
# a.get_info()
# a.minus_balance(1500)
# a.get_info()
                              #наследование

# class Animal:
#     def __init__(self, number_of_legs):
#         self.number_of_legs = number_of_legs
#
# class Dog(Animal):
#     def get_dog(self):
#         print(f"у собаки {self.number_of_legs} ноги")
# b = Dog(4)
# b.get_dog()
# class Bird(Animal):
#     def get_bird(self):
#         print(f'чымчыкта {self.number_of_legs} бут болот')
#
# c = Bird(2)
# c.get_bird()



# class Instrument:
#     def __init__(self, volume):
#         self.volume = volume
#     def set_volume(self, volume):
#         self.volume = volume
# class Gitara(Instrument):
#     def pley_gitare(self):
#         print(f"я играю на гитаре и моя громкость {self.volume} ")
# class Piano(Instrument):
#     def play_piano(self):
#         print(f"я играю на пинино и моя громкость {self.volume}")
# a = Instrument(5)
# a.set_volume(10)
# print(a.volume)
# b = Gitara(15)
# c = Piano(10)
# b.pley_gitare()
# c.play_piano()
# c.set_volume(54)
# c.play_piano()

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def set_name(self, name):
#         self.name = name
#     def set_price(self, price):
#         self.price = price
#
# class Vegetable(Product):
#     def get_info(self):
#         print(f"вы готовите {self.name} за {self.price}")
# class Fruits(Product):
#     def get_info(self):
#         print(f"вы кушаете {self.name} за {self.price}")
# a = Vegetable("картошка", 34)
# a.get_info()
# b = Fruits("банан", 25)
# b.get_info()

# class Car:
#     def __init__(self, brand, price, speed):
#         self.brand = brand
#         self.price = price
#         self.speed = speed
#     def set_brand(self, brand):
#         self.brand =brand
#     def set_price(self, price):
#         self.price = price
#     def set_speed(self, speed):
#         self.speed = speed
# class BMW(Car):
#     def get_info(self):
#         print(f"бул машина bmw {self.brand} баасы {self.price}$ саатына {self.speed} км ылдамдыкта журот")
# class Suparu(Car):
#     def get_info(self):
#         print(f"бул машина subaru {self.brand} баасы {self.price}$ саатына {self.speed} км ылдамдыкта журот")
#
# a = BMW("x5", 25000, 250)
# a.get_info()
# b = Suparu("forestr", 15000, 220)
# b.get_info()
# a.set_brand("x7")
# a.get_info()

# class Person:
#     def __init__(self, name, age, job):
#         if self.__check_value(name) and self.__check_value_int(age) and self.__check_value(job):
#             self.__name = name
#             self.__age = age
#             self.__job = job
#         else:
#             raise ValueError("вы указали тип не правильно")
#     def __check_value(self, value):
#         return type(value) in (str, )
#     def __check_value_int(self, value):
#         return type(value) in (int, )
#     def get_info(self):
#         print(self.__name, self.__age, self.__job)
# a = Person("Agahan", 18, "it")n
# a.get_info()

