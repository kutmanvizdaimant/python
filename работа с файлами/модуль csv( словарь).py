# import csv
#
# peaple = [
#     ['kutman', 23],
#     ['ainazik', 16],
#     ['agahan', 18],
#     ['aidai', 25],
#     ['islam', 55],
#     ['talgat', 34],
#     ['syimyk', 23],
# ]

# new_peaple = []
# for i in peaple:
#     if 20 < i[1] < 30:
#         new_peaple.append(i)

# print(new_peaple)
# FILENAME = 'new_generation.csv'
# with open(FILENAME, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(new_peaple)
#
# with open(FILENAME, 'r', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[0], '-', row[1])


import csv
FILENAME = 'only_men.csv'
men = []
a = [
    {'name': 'agahan',  'gender': 'm'},
    {'name': 'ainazik', 'gender': 'g'},
    {'name': 'kutman',  'gender': 'm'},
    {'name': 'aidai',   'gender': 'g'},
    {'name': 'islam',   'gender': 'm'},
]
for i in a:
    if (i['gender']) == 'm':
        men.append(i)
print(men)


with open(FILENAME, 'w', newline='') as file:
    columns = ['name', 'gender']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(men)

with open(FILENAME, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], '-', row['gender'])

# Одним из распространенных файловых форматов, которые
# хранят в удобном виде информацию, является формат csv.
# Каждая строка в файле csv представляет отдельную запись
# или строку, которая состоит из отдельных столбцов, разделенных
# запятыми. Собственно поэтому формат и называется Comma Separated
# Values. Но хотя формат csv - это формат текстовых файлов, Python
# для упрощения работы с ним предоставляет специальный встроенный модуль csv.

import csv

FILENAME = "users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)


# В файл записывается двухмерный список - фактически таблица,
# где каждая строка представляет одного пользователя. А каждый
# пользователь содержит два поля - имя и возраст. То есть фактически
# таблица из трех строк и двух столбцов.
#
# При открытии файла на запись в качестве третьего параметра
# указывается значение newline="" - пустая строка позволяет корректно
# считывать строки из файла вне зависимости от операционной системы.
#
# Для записи нам надо получить объект writer, который возвращается
# функцией csv.writer(file). В эту функцию передается открытый файл.
# А собственно запись производится с помощью метода writer.writerows(users)
# Этот метод принимает набор строк. В нашем случае это двухмерный список.
#
# Если необходимо добавить одну запись, которая представляет собой одномерный
# список, например, ["Sam", 31], то в этом случае можно вызвать метод writer.writerow(user)

# Для чтения из файла нам наоборот нужно создать объект reader:

import csv

FILENAME = "users.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])

# В примере выше каждая запись или строка
# представляла собой отдельный список, например,
# ["Sam", 31]. Но кроме того, модуль csv имеет
# специальные дополнительные возможности для работы
# со словарями. В частности, функция csv.DictWriter()
# возвращает объект writer, который позволяет записывать
# в файл. А функция csv.DictReader() возвращает объект
# reader для чтения из файла. Например:

import csv

FILENAME = "users1.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"name": "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])