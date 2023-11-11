from typing import Any


class Student:
    def __init__(self, name='хуй', age='много'):#дефолтные значения сработают, если экз создать без атрибутов
        self.name = name
        self.age = age

    @property
    # созадем аттр-свойство возращающее кортеж с инфо
    def get_info(self):
        self.info = {'name': self.name.capitalize(), 'age': self.age}
        return self.info
    
    @get_info.setter# даем возможность менять атрибут get_info
    def get_info(self, n_name):
        self.name, self.age = n_name
        
    @get_info.deleter # при удалении фтрибута(свойства) значения атрибутов класса изменятся на указаные
    # в делитере, что помогает избежать ошибки
    def get_info(self):
        self.name = 'удалено'
        self.age = 'удалено'

x1 = Student('ivan', 33)
print(x1.get_info)
x1.get_info = "ф",2
print(x1.get_info)
del x1.name
print(getattr(x1, 'name', None))
del x1.get_info
print(x1.age)
print(x1.get_info)