# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_info(self):
#         print(f"Имя: {self.name}\tвозраст: {self.age}")
# tom = Person("kutman", 28)
# tom.display_info()

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1
#
#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print("Недоступный возраст")
#
#     def get_age(self):
#         return self.__age
#     def get_name(self):
#         return self.__name
#     def display_info(self):
#         print(f"Имя: {self.__name}\tвозраст: {self.__age}")
# tom = Person("tom")
# tom.display_info()
# tom.set_age(-324)
# tom.set_age(23)
# tom.display_info()

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
