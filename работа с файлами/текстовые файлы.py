# with open("hello.txt", "w") as file:
#     file.write("hello world")
#
# with open("hello.txt", "a") as file:
#     file.write("\ngood bye, world")

# Дозапись выглядит как добавление строку к
# последнему символу в файле, поэтому, если
# необходимо сделать запись с новой строки,
# то можно использовать эскейп-последовательность
# "\n". В итоге файл hello.txt будет иметь следующее содержимое:

# Еще один способ записи в файл представляет
# стандартный метод print(), который применяется для вывода данных на консоль:

# with open("hello.txt", "w") as hello_file:
#     print("Kutman asdas da asd ", file=hello_file)

# Для вывода данных в файл в метод print в качестве
# второго параметра передается название файла через
# параметр file. А первый параметр представляет записываемую в файл строку.

# Чтение файла
# Для чтения файла он открывается с режимом r (Read), и затем мы можем считать его содержимое различными методами:
#
# readline(): считывает одну строку из файла
#
# read(): считывает все содержимое файла в одну строку
#
# readlines(): считывает все строки файла в список

# with open("hello.txt", "r") as file:
#     for line in file:
#         print(line, end='')

# Несмотря на то, что мы явно не применяем метод
# readline() для чтения каждой строки, но в при
# переборе файла этот метод автоматически вызывается
# для получения каждой новой строки. Поэтому в цикле
# вручную нет смысла вызывать метод readline. И поскольку
# строки разделяются символом перевода строки "\n", то чтобы
# исключить излишнего переноса на другую строку в функцию print
# передается значение end="".
#
# Теперь явным образом вызовем метод readline() для чтения отдельных строк:

# with open("hello.txt", "r") as file:
#     str1 = file.readline()
#     print(str1, end="")
#     str2 = file.readline()
#     print(str2)

# Если файл небольшой, то его можно разом считать с помощью метода read():

# with open("hello.txt", "r") as file:
#     content = file.read()
#     print(content)

# # И также применим метод readlines() для считывания всего файла в список строк:
# with open("hello.txt", "r") as file:
#     contents = file.readlines()
#     str1 = contents[3]
#     str2 = contents[1]
#     print(str1, end='')
#     print(str2)

# # При чтении файла мы можем столкнуться с тем,
# # что его кодировка не совпадает с ASCII. В этом
# # случае мы явным образом можем указать кодировку с помощью параметра encoding:
#
# filename = "hello.txt"
# with open(filename, encoding="utf8") as file:
#     text = file.read()
#
# Теперь напишем небольшой скрипт, в котором
# будет записывать введенный пользователем массив
# строк и считывать его обратно из файла на консоль:

# имя файла
FILENAME = "messages.txt"
# определяем пустой список
messages = []

for i in range(4):
    message = input("Введите строку " + str(i + 1) + ": ")
    messages.append(message + "\n")

# запись списка в файл
with open(FILENAME, "w") as file:
    for message in messages:
        file.write(message)

# # считываем сообщения из файла
print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")