class Rectangle:
    def __init__(self, wigth, height) -> None:
        self.wigth = wigth
        self.height = height

    @property
    def area(self):
        return self.wigth * self.height
    
# является обычным методом а не свойством. просто изменяет базовые значения
    def resize(self, *args):
        if len(args) == 2:
            wigth = args[0]
            height = args[1]
        else:
            raise ValueError('слишком многа букав!')
        if wigth > 0 and height > 0:
            self.wigth = wigth
            self.height = height
        else:
            raise ValueError('HEJIb39I')

    @area.deleter
    def area(self):
        print('значения сброшены')
        self.wigth = 1
        self.height = 2


c1 = Rectangle(11, 12)
# print(c1.area)
# c1.resize(-1,11)
# print(c1.area)
del c1.area
print(c1.area)