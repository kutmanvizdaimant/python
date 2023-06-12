# 1) - ушул сандардын общий суммасын табыныз
# 2) string = “Сегодня у меня все получится” - “Сегодня деген созду алып анын ордуна “Завтра”

# a = "123451"
# b = 0
# for i in a:
#     b += int(i)
# print(b)

# string = "Сегодня у меня все получится"
# a = string.replace("Сегодня", "Завтра")
# print(a)

# Условный оператор
# 1) - нечетный сандардын общий суммасын табыныз

# a = [1, 2, 3, 4, 12, 15, 16, 19, 20, 23]
# b = 0
# for i in a:
#     if i % 2 == 1:
#         b += i
# print(b)

# 2) -общий суммасын чыгарып бергиле
# a = ["agahan", "kutman", "aidai", "ainazik", "islam", "syimyk", "nurtilek", "cholponbek"]
# b = []
# c = 0
# for i in a:
#     if len(i) > 7:
#         b.append(len(i))
# for i in b:
#     c += i
# print(c)


# a = ["agahan", "kutman", "aidai", "ainazik", "islam", "syimyk", "nurtilek", "cholponbek"]
# b = []
# for i in a:
#     if "a" in i:
#         b.append(i)
# print(b)

# a = ["agahan", "kutman", "aidai", "ainazik", "islam", "syimyk", "nurtilek", "cholponbek"]
# for i in a:
#     if len(i) > 5 and i.endswith("k"):
#         print(i)

# password = ""
# while password != 'тынчтык':
#     password = input("введите пароль")
#     if password != "тынчтык":
#         print("неверный пароль. попробуйте снова")
# else:
#     print("туура пароль")

# 1)  - строканын ичиндеги сандарды гана консольго чыгарыныз
# string = "asdas1231asdasd"
# for i in string:
#     if i.isnumeric():
#         print(i)

# 2)- строканын ичиндеги тамгаларды гана жаны списокко кошуп анан списокту консольго чыгарыныз

# string = "asdas1231asdasd"
# b = []
# for i in string:
#     if i.isalpha():
#         b.append(i)
# print(b)

# 1)  - списоктон экинчи чон сан жана экинчи кичинекей санды табып,
# консольго ушул эки сандын суммасын чыгарыныз.

# b = [1, 13, 14, 43, 2, 5, 10, 12, 19]
# b.sort()
# a = b[-2] + b[1]
# print(a)

# 2)- списоктон “cholponbek” деген аттын ордуна “aicholpon” деп алмаштырып койгула.
# a = ["agahan", "kutman", "aidai", "ainazik", "islam", "syimyk", "nurtilek", "cholponbek"]
# a[7] = "aicholpon"
# print(a)

# 1)  - ушул эки словарьды бир словарьга кошунуз.

# a = { "Kyrgyzstan": "Bishkek", "Russia": "Moscow", "Italy": "Rom"}
# b = {"Canada": "Ottava", 'USA': "Washington", "France": "Paris"}
# b.update(a)
# print(a)
# print(b)

# 2)  - словарьдан оценкалардын среднее арифметическое табыныз.
# #
# students = {
#     "kutman" : 4.5,
#     "aidai": 3.9,
#     "ainazik": 4.1,
#     "islam": 4.2,
#     "syimyk": 4.6,
#     "cholponbek": 4.9
# }
#
# b = 0
# for x, y in students.items():
#     b += y
# print(b//len(students))


