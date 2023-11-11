class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        
# На лицо проблема: переменные иниц. один раз и чтобы получить
# измененую фамилию нужно создавать метод.
    def get_fullname(self):
# метод позволяет получить денимически меняющиеся данные 
# посредством своего вызова
        self.fullname = self.name + ' ' + self.surname
        return self.fullname

c =  Person('I', 'A')
c.surname = 'oo'
print(c.surname)
print(c.get_fullname())
c.surname = '00'
print(c.get_fullname())
# м
class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
# метод с декоратором это свойство разница в том, что теперь он
# вызываться, как обычный атрибут. То есть просто через точку.
    @property
    def get_fullname(self):
        return f'{self.name} {self.surname}'
    
a = Person('Vaka', 'Maka')
print(a.name)
print(a.get_fullname)
#Это не метод, обычный атрибут, который определяется динамически
# то есть, в момент его вызова.
a.name = 'Chaka'
print(a.get_fullname)