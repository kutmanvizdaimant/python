# names = ['agahan', 'beksultan', 'erzhan', 'shulamita', 'aicholpon', 'askar', 'tumar', 'ainazik']
#
# FILENAME = "names.txt"
# messages = []
#
# # запись списка в файл
# with open(FILENAME, "w") as file:
#     for message in names:
#         file.write(message + '\n')
#
# import os
# a = 0
# print("Считанные сообщения")
#
#
# with open(FILENAME, "r") as file:
#     for message in file:
#         if message.startswith('a'):
#             a += 1
#
# def main():
#     filename = input("Введите путь к файлу: ")
#     if not os.path.exists(filename): # exists - сущесвует
#         print("Указанный файл не существует")
#     else:
#         print(f"Кол-во слов: {len(names)}")
#         print(f'коль во слов который начинается а {a}')
#
# main()

# numbers = ["13", "14", "15", "16", "29", "30", "28", "27", "31", "33", "22"]
# FILENAME = "numbers.txt"
# import os
# with open(FILENAME, "w") as file:
#     for i in numbers:
#         file.write(i + '\n')
# a = []
# def get_even_number(FILENAME):
#     b = 0
#     with open(FILENAME, "r") as file:
#         for i in file:
#             if int(i) % 2 == 0:
#                 b += 1
#     return b
#
# def main():
#     filename = input("Введите путь к файлу: ")
#     if not os.path.exists(filename):
#         print("Указанный файл не существует")
#     else:
#         print(f"Кол-во счетных чисел : {get_even_number(filename)}")
#         print(f' общ коль-во {len(numbers)}')
# main()

