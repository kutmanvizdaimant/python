#  insert = добавляем набор элементов [3, "kutman"]
# append = добавляем на вторую позицию
# extend = добавляем несколько элементов ["roma", "beknazar"]
# pop = удаляет  по индексу(2)
# remove = удаляет по имени
# clear(a) = удаляем все элементы
#  count = санайбыз количество
# sort = осуу тартибинде
# reverse = алмаштыруу тартбин
# copy = ккопировать

a = ["Agahan", "Aidai", "islam", "Cholponbek"]
a[0] = "Ainazik"
print(a)

# a = ["Agahan", "Aidai", "islam", "Cholponbek", "Nurtilek", "kutman", "ainazik", 'ermat']
# b = a[0:7:3]
# print(b)

# a = ["tom", "bob", "Alica", "Sam", "bill", "Kate", "Mike"]
# del a[1]
# print(a)
# del a[:3]
# print(a)
# del a[1:]
# print(a)

# a = ["Agahan", "Agahan", "Islam", "kutman", "ainazik", "nurtilek", "nurtilek"]
# for i in a:
#     if a.count(i) > 1:
#         a.remove(i)
# print(a)


# a = [1, 2, 5, 85, 56]
# b= 0
# for i in a:
#     if i % 2 == 0:
#         b += i
# print(b)

# a = ["agahan", "halk", "ainazik", "islam", "kutman"]
# for i in a:
#     if len(i) > 6:
#         print(i)

# a = [3, 7, 16, 78, 23, 90]
# b = [41, 3,  90, 16, 15, 43]
# for i in a:
#     if i in b:
#         print(i)

# a = []
# for i in range(5):
#     b = int(input())
#     a.append(b)
# print(f'min: {min(a)}')
# print(max(a))

# a = []
# for i in range(10):
#     b = int(input())
#     if b % 2 == 0:
#         a.append(b)
# print(a)

# a = [2, 3, 4, 19, 20, 23, 67]
# b = 0
# for i in a:
#     b += i
# print(b // len(a))

# a = []
# while True:
#     b = input()
#     if b.startswith("a"):
#         a.append(b)
#     elif b == "uikuchu":
#         break
# print(a)

# a = [5, 10, 15, 20, 7, 25, 30, 9, 6]
# b = max(a)
# a.remove(max(a))
# print(max(a))

# a = [5, 10, 15, 20, 7, 25, 30, 9, 6]
# a.sort()
# print(a[-2])

# a = [3, 4, 5, 7, 8, 4, 5, 8]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# a = ["Agahan", "Islgghkkln", "kutman", "ainazik", "nurtilek", "nurtilek"]
# b = list()
# for i in a:
#     if len(i) > 7:
#         b.append(i)
# print(b)

# a = [3, 4, 5, 12, 13, 15, 23, 30, 23]
# a.reverse()
# print(a[-2])
