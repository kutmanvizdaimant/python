# Создание и закрытие файла
# from zipfile import ZipFile
#
# myzip = ZipFile("metanit.zip", "w")
#
# from zipfile import ZipFile
#
# myzip = ZipFile("metanit.zip", "w")
# myzip.close()

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "w") as myzip:
#     pass

# Запись файлов в архив

# write(filename, arcname=None, compress_type=None, compresslevel=None)

# Первый параметр представляет файл, который записиывается в архив.
# Второй параметр - arcname устанавливает произвольное имя для файла
# внутри архива (по умолчанию это само имя файла). Третий параметр - compress_
# type представляет тип сжатия, а параметр compresslevel - уровень сжатия.
#
# Например, запишем в архив "metanit.zip" файл "hello.txt" (который, как
# предполагается, находится в той же папке, где и текущий скрипт python):

from zipfile import ZipFile

with ZipFile("metanit.zip", "a") as myzip:
    content = 'Ainazik'
    myzip.writestr("ainazik.txt", content)

# from zipfile import ZipFile

# with ZipFile("metanit.zip", "w") as myzip:
#     myzip.write("hello.txt")
    # myzip.write("forest.jpg")


# Стоит отметить, что по умолчанию сжатие не применяется.
# Но при необходимости можно применить какой-нибудь способ сжатия и уровень сжатия"

# from zipfile import ZipFile, ZIP_DEFLATED
#
# with ZipFile("metanit.zip", "w", compression=ZIP_DEFLATED, compresslevel=3) as myzip:
#     myzip.write("hello.txt")

# Необходимо учитывать, что если мы попробуем добавить в архив файлы с уже
# имеющимися именами, то консоль выведет предупреждение. Чтобы избежать
# наличия файлов с дублирующимися именами можно через второй папаметр метода
# write явным образом определить для них уникальное имя внутри архива:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "a") as myzip:
#     myzip.write("hello.txt", "hello1.txt")
#     myzip.write("hello.txt", "hello2.txt")
#     myzip.write("hello.txt", "hello3.txt")


# Получение информации о файлах в архиве

# Метод infolist() возвращает информацию о
# файлах в архиве с виде списка, где каждый
# отдельный файл представлен объектом ZipInfo:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "a") as myzip:
#     print(myzip.infolist())


# Класс ZipInfo предоставляет ряд атрибутов для хранения информации о файле. Основные из них:
#
# filename: название файла
#
# date_time: дата и время последнего изменения файла в виде кортежа в формате
# (год, месяц, день, час, минута, секунда)
#
# compress_type: тип сжатия
#
# compress_size: размер после сжатия
#
# file_size: оригинальный размер файла до сжатия

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     for item in myzip.infolist():
#         print(f"File Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")


# С помощью метода is_dir() можно проверить, является ли элемент в архиве папкой:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     for item in myzip.infolist():
#         if (item.is_dir()):
#             print(f"Папка: {item.filename}")
#         else:
#             print(f"Файл: {item.filename}")


# Если надо получить только список имен входящих в архив файлов, то применяется метод namelist():

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     for item in myzip.namelist():
#         print(item)


# С помощью метода getinfo() можно получить данные по одному из архивированных файлов,
# передав в метод его имя в архиве. Результат метода - объект ZipInfo:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     try:
#         hello_file = myzip.getinfo("hello.txt")
#         print(hello_file.file_size)
#     except KeyError:
#         print("Указанный файл отсутствует")

# Если в архиве не окажется элемента с указанным именем, то метод сгенерирует ошибку KeyError.

# Извлечение файлов из архива

# Для извлечения всех файлов из архива применяется метод extractall():

# extractall(path=None, members=None, pwd=None)
# Первый параметр метода устанавливает каталог для извлечения
# архива (по умолчанию извлечение идет в текущий каталог).
# Параметр members представляет список строк - список названий
# файлов, которые надо извлечт из архива. И третий параметр - pwd
# представляет пароль, в случае если архив закрыт паролем.

# Например, извлечем все файлы из архива:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     myzip.extractall(path="agahan", members=['hello.txt', 'hello1.txt']) # path - путь


# # Извлечение в определенную папку:
#
# myzip.extractall(path="metanit")
#
# Извлечение части файлов:

# извлекаем файлы  "hello.txt", "forest.jpg" в папку "metanit2"
# myzip.extractall(path="agahan", members=["hello.txt", "hello1.txt"])

# Для извлечения одного файла применяется метод extract(),
# в который в качестве обязательного параметра передается имя извлекаемого файла:

# myzip.extract("hello.txt")

# Считывание файла

# Метод read() позволяет считать содержимое файла из архива в набор байтов:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     content = myzip.read("hello1.txt")
#     print(content)

# Открытие файла

# Метод open() позволяет открывать отдельные файлы из архива без непосредственного их извлечения:

# open(name, mode='r', pwd=None, *, force_zip64=False)

# В качестве первого обязательного параметра передается имя
# файла внутри архива. Второй параметр - mode устанавливает
# режим открытия. Параметр pwd задает пароль, если файл
# защищен паролем. И параметр force_zip64 при значении True
# позволяет открывать файлы больше 4 Гб.
#
# Этот файл может быть полезен для манипулирования файлом,
# например, для считывания его содержимого или, наоборот,
# для записи в него. Например, откроем файл и считаем его содержимое:


# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "a") as myzip:
#     # записываем в архив новый файл "hello5.txt"
#     with myzip.open("hello5.txt", "w") as hello_file:
#         encoded_str = bytes("Kutman...", "UTF-8")
#         hello_file.write(encoded_str)
# Создание и закрытие файла
# from zipfile import ZipFile
#
# myzip = ZipFile("metanit.zip", "w")
#
# from zipfile import ZipFile
#
# myzip = ZipFile("metanit.zip", "w")
# myzip.close()

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "w") as myzip:
#     pass

# Запись файлов в архив

# write(filename, arcname=None, compress_type=None, compresslevel=None)

# Первый параметр представляет файл, который записиывается в архив.
# Второй параметр - arcname устанавливает произвольное имя для файла
# внутри архива (по умолчанию это само имя файла). Третий параметр - compress_
# type представляет тип сжатия, а параметр compresslevel - уровень сжатия.
#
# Например, запишем в архив "metanit.zip" файл "hello.txt" (который, как
# предполагается, находится в той же папке, где и текущий скрипт python):

from zipfile import ZipFile

with ZipFile("metanit.zip", "a") as myzip:
    content = 'Ainazik'
    myzip.writestr("ainazik.txt", content)

# from zipfile import ZipFile

# with ZipFile("metanit.zip", "w") as myzip:
#     myzip.write("hello.txt")
    # myzip.write("forest.jpg")


# Стоит отметить, что по умолчанию сжатие не применяется.
# Но при необходимости можно применить какой-нибудь способ сжатия и уровень сжатия"

# from zipfile import ZipFile, ZIP_DEFLATED
#
# with ZipFile("metanit.zip", "w", compression=ZIP_DEFLATED, compresslevel=3) as myzip:
#     myzip.write("hello.txt")

# Необходимо учитывать, что если мы попробуем добавить в архив файлы с уже
# имеющимися именами, то консоль выведет предупреждение. Чтобы избежать
# наличия файлов с дублирующимися именами можно через второй папаметр метода
# write явным образом определить для них уникальное имя внутри архива:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "a") as myzip:
#     myzip.write("hello.txt", "hello1.txt")
#     myzip.write("hello.txt", "hello2.txt")
#     myzip.write("hello.txt", "hello3.txt")


# Получение информации о файлах в архиве

# Метод infolist() возвращает информацию о
# файлах в архиве с виде списка, где каждый
# отдельный файл представлен объектом ZipInfo:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "a") as myzip:
#     print(myzip.infolist())


# Класс ZipInfo предоставляет ряд атрибутов для хранения информации о файле. Основные из них:
#
# filename: название файла
#
# date_time: дата и время последнего изменения файла в виде кортежа в формате
# (год, месяц, день, час, минута, секунда)
#
# compress_type: тип сжатия
#
# compress_size: размер после сжатия
#
# file_size: оригинальный размер файла до сжатия

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     for item in myzip.infolist():
#         print(f"File Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")


# С помощью метода is_dir() можно проверить, является ли элемент в архиве папкой:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     for item in myzip.infolist():
#         if (item.is_dir()):
#             print(f"Папка: {item.filename}")
#         else:
#             print(f"Файл: {item.filename}")


# Если надо получить только список имен входящих в архив файлов, то применяется метод namelist():

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     for item in myzip.namelist():
#         print(item)


# С помощью метода getinfo() можно получить данные по одному из архивированных файлов,
# передав в метод его имя в архиве. Результат метода - объект ZipInfo:

# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     try:
#         hello_file = myzip.getinfo("hello.txt")
#         print(hello_file.file_size)
#     except KeyError:
#         print("Указанный файл отсутствует")

# Если в архиве не окажется элемента с указанным именем, то метод сгенерирует ошибку KeyError.

# Извлечение файлов из архива

# Для извлечения всех файлов из архива применяется метод extractall():

# extractall(path=None, members=None, pwd=None)