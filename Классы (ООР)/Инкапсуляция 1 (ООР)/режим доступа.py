class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def __check_value(self, x):
        return type(x) in (int, float)
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("кординаты должны быть числами")
    def get_coord(self):
         return self.__y, self.__x
pt = Point(1, 3)
# print(pt.__x)
# pt.set_coord("kutman", 20)
print(pt.get_coord())