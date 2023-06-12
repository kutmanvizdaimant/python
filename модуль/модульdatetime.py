# Класс date
# Для работы с датами воспользуемся классом date,
# который определен в модуле datetime. Для создания
# объекта date мы можем использовать конструктор date,
# который последовательно принимает три параметра: год, месяц и день.

# import datetime
#
# yesterday = datetime.date(2017, 5, 2)
# print(yesterday)  # 2017-05-02

# Если необходимо получить текущую дату, то можно воспользоваться методом today():

# from datetime import date
#
# today = date.today()
# print(today)  # 2017-05-03
# print("{}.{}.{}".format(today.day, today.month, today.year))
# print(f"{today.day}.{today.month}.{today.year}")

# С помощью свойств day, month, year можно получить соответственно день, месяц и год

# Класс time
# За работу с временем отвечает класс time.
# Используя его конструктор, можно создать объект времени:

# time([hour] [, min] [, sec] [, microsec])

# from datetime import time
#
# current_time = time()
# print(current_time)  # 00:00:00
#
# current_time = time(16, 25)
# print(current_time)  # 16:25:00
#
# current_time = time(16, 25, 45)
# print(current_time)  # 16:25:45

# Класс datetime
# Класс datetime из одноименного модуля
# объединяет возможности работы с датой и временем.
# Для создания объекта datetime можно использовать следующий конструктор:

# datetime(year, month, day [, hour] [, min] [, sec] [, microsec])

# Первые три параметра, представляющие год,
# месяц и день, являются обязательными.
# Остальные необязательные, и если мы не
# укажем для них значения, то по умолчанию они инициализируются нулем.

# from datetime import datetime
#
# deadline = datetime(2017, 5, 10)
# print(deadline)  # 2017-05-10 00:00:00
#
# deadline = datetime(2017, 5, 10, 4, 30)
# print(deadline)  # 2017-05-10 04:30:00

# Для получения текущих даты и времени можно вызвать метод now():

# from datetime import datetime
#
# now = datetime.now()
# print(now)  # 2017-05-03 11:18:56.239443
#
# print("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))  # 3.5.2017  11:21
#
# print(now.date())
# print(now.time())

# Преобразование из строки в дату
# strptime(str, format)

# %d: день месяца в виде числа
#
# %m: порядковый номер месяца
#
# %y: год в виде 2-х чисел
#
# %Y: год в виде 4-х чисел
#
# %H: час в 24-х часовом формате
#
# %M: минута
#
# %S: секунда

from datetime import datetime

deadline = datetime.strptime("2023/02/06", "%Y/%d/%m")
print(deadline)  # 2017-05-22 00:00:00

deadline = datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)  # 2017-05-22 12:30:00

deadline = datetime.strptime("05-22-2017 12:30", "%m-%d-%Y %H:%M")
print(deadline)  # 2017-05-22 12:30:00