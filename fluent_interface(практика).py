class Person:
    def __init__(self, name) -> None:
        self.name = name
        
    def set_name(self, name):
        self.name = name
        return Person(self.set_name)
        
    def set_age(self, age):
        return self.__class__(age)
    
    def filter(self, fn):
        return Person(list(filter(fn, self.coll)))
    
    def all(self):
        return f'{self.name} ему {self.age} лет'
    
baka = Person('s')

print(baka.set_name("Антон").set_age('11').all())