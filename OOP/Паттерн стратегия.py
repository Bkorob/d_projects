class A: # обозначаем стратегию 1
    def data_p(self, data, *args):
        key = args[0]
        return data.get(key, 'lol')
    

class B: # стратегию 2
    def data_p(self, data, *args):
        key = args[0]
        return data.get(key, 'lol') + 100
    

class C: # управляющий класс имеющий метод, принимающий класс стратегию
    def __init__(self, data):
        self.data = data
    @property
    def get_data(self): # создание метода с помощью декоратора класса
        return self.data
    
    def get_val(self, cls): # метод-оператор класса. принимет абстрактный класс-стратегию
        #  и возращает результат, в зависимости от выбранной стратегии.
        return cls.data_p(self.get_data, 'p')

c = C({'p': 100})
b = B()
a = A()
print(c.get_val(b)) # стратегия 1
print(c.get_val(a)) # стратегия 2