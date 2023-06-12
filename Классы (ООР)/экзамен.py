class Vehicle:
    def __init__(self, marka, model, year, speed):
        self.marka = marka
        self.model = model
        self.year = year
        self.speed = speed
    def get_info(self):
        print(f'marka: {self.marka}, model: {self.model}, year: {self.year}, speed: {self.speed}')
    def acceleration(self):
        print('это машина может ускорится до 350км/ч')
    def deceleration(self):
        print('это машина может замедляться до 3км/ч')

class Car(Vehicle):
    def __init__(self, marka, model, year, speed, type_model, count_passengers):
        super().__init__(marka, model, year, speed)
        self.type_model = type_model
        self.count_passengers = count_passengers
    def set_type_model(self, value):
        self.type_model = value
    def set_count_passengers(self, value):
        self.count_passengers = value
class Truck(Vehicle):
    def __init__(self, marka, model, year, speed, type_model, carrying_capacity):
        super().__init__(marka, model, year, speed)
        self.type_model = type_model
        self.carrying_capacity = carrying_capacity

    def set_type_model(self, value):
        self.type_model = value

    def set_carrying_capacity(self, value):
        self.carrying_capacity = value
class Buss(Vehicle):
    def __init__(self, marka, model, year, speed, disabled, count_passengers):
        super().__init__(marka, model, year, speed)
        self.disabled = disabled
        self.count_passengers = count_passengers
    def check_disabled(self,):
        return self.disabled
    def set_count_passengers(self, value):
        self.count_passengers = value
a1 = Vehicle()

class UserAccount:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
    def check_password(self, old_password):
        if self.__password == old_password:
            return True
        else:
            return False
    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
        else:
            print('неправильно ввели пароль')
a1 = UserAccount('agahan', 'agahan123')
a1.check_password('agahan123')
a1.change_password('agahan123', 'kutman123')

class Instrument:
    def play_music(self):
        pass
class Gitara(Instrument):
    def play_music(self):
        print(f"я играю на гитаре  ")
class Piano(Instrument):
    def play_music(self):
        print(f"я играю на пинино ")
class Baraban(Instrument):
    def play_music(self):
        print(f"я играю на barabane ")
a1 = Gitara()
a2 = Piano()
a3 = Baraban()
b = [a1, a2, a3]
for i in b:
    i.play_music()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Point):
            return self.x + other.x, self.y + other.y
        else:
            raise ValueError('owibka')
    def __mul__(self, other):
        if isinstance(other, Point):
            return self.x * other.x, self.y * other.y
        else:
            raise ValueError('owibka')
    def __sub__(self, other):
        if isinstance(other, Point):
            return self.x - other.x, self.y - other.y
        else:
            raise ValueError('owibka')
a1 = Point(5, 6)
a2 = Point(6, 5)
print(a1+a2)
print(a1*a2)
print(a1-a2)