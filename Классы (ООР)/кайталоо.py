# class Product:
#     def __init__(self, name, price, quantity):
#         self.__name = name
#         self.__price = price
#         self.__quantity = quantity
#     def add_product(self, value):
#         if self.__check_value(value):
#             self.value = value
#         else:
#             raise ValueError('только сан')
#         self.__quantity += value
#         print(f"тепер ваш продукт {self.__quantity}")
#     def __check_value(self, value):
#         return type(value) in (int,)
#     def set_new_price(self, price):
#         if self.__check_value(price):
#             self.__price = price
#         else:
#             raise ValueError("кординаты должны быть числами")
#     def get_info(self):
#         print(f'name: {self.__name} price: {self.__price} quantity: {self.__quantity}')
#
# a = Product('igruwka', 150, 14)
# a.add_product(5)
# a.set_new_price("200")
# a.get_info()

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise ValueError('экземпляры болуш керек')
        else:
            if self.rank == other.rank and self.suit == other.suit:
                print("ekoo ten barabar")
            elif self.rank != other.rank and self.suit == other.suit:
                print('suitter biri birine barabar')
            elif self.rank == other.rank and self.suit != other.suit:
                print("ranktar biri birine barabar")
            else:
                self.get_info()
                print('barabar emes')
    def get_info(self):
        print(f"rank: {self.rank}, suit: {self.suit}")

a = Card("karol", "jurok")
b = Card('dama', 'jurok')
d = Card('karol', 'chyrym')
e = Card('karol', 'jurok')
a == b
b == d
d == e
e == a
b.get_info()