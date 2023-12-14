from pprint import pprint
class User: # определяем класс принимающий имя
    def __init__(self, name):
        self.name = name

    def get_name(self): # метод класса возращающий значение имени
        return self.name
# a = User('v')
# methods = getattr(a, '__class__').__dict__
# pprint(methods)
def call_method(self, method_name, *args): # функция принимает имя объекта класса, метод и *args
    methods = getattr(self, '__class__').__dict__ # получаем словарь методов класса объекта self
    pprint(methods)
    method = methods.get(method_name)
    # присваиваем получение метода(аргумент) из словаря атрибутов 
    if method: # если присвоили:
        return method(self, *args) # возвращаем полученный метод класса 
    # (в нашем случае self.get_name())
    raise Exception('No method error')

call_method(User('Mike'), 'get_name')