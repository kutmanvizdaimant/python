# def extend_list(lst: list):
#     if lst == []:
#         raise Exception('список не должен быть пустым')
#     a = []
#     b = []
#     for i in lst:
#         if i % 2 == 0:
#             a.append(i)
#     for i in lst:
#         if i % 2 == 1:
#             b.append(i)
#     print(a+b)
# extend_list([1, 2, 34, 12, 3, 4])
# extend_list([])

# b = "AOUIYEaiouye"
# a = input()
# c = []
# if a == "":
#     raise Exception("вы обеязательно должны вводит что то")
#
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# def sum_string(str1, str2):
#     a = 0
#     b = 0
#     try:
#         for i in str1:
#             a += int(i)
#
#         for i in str2:
#             b += int(i)
#         print(a+b)
#     except ValueError:
#         print("error")
# sum_string("14567", "8976")

# def find_avg(*number):
#     for i in number:
#         if type(i) != int:
#             raise Exception("siz type error bolup kaldy")
#     a = sum(number)/len(number)
#     print(a)
#
# find_avg(1, 2, "jhjh", 4, 5, 6, 12, 21, 14)

# a = input()
# b = input()
# try:
#     c = int(a)/int(b)
#     print(c)
# except ValueError:
#     print("valueerror")
# except ZeroDivisionError:
#     print("zerodivisionerror")

