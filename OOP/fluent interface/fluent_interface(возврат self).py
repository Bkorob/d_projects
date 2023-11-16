class Collection: #возврат self из методов учавствующих в постороении цепей
    def __init__(self, coll):
        self.coll = coll

    def map(self, fn):
        self.coll = list(map(fn, self.coll))
        return self # возвращается значение, а ссылка на него.

    def filter(self, #она же и принимается \
                fn): 
        self.coll = list(filter(fn, self.coll))
        print(self) # <__main__.Collection object at 0x10e572c50> - ССЫЛКА
        return self

    # Возвращает саму коллекцию, а не self.
    # Этот метод всегда последний в цепочке вызовов Collection.
    def all(self):
        return self.coll 

cars = Collection([
    {'model': 'rapid', 'year': 2016},
    {'model': 'rio', 'year': 2013},
    {'model': 'mondeo', 'year': 2011},
    {'model': 'octavia', 'year': 2014}
])

cars.filter(lambda car: car['year'] > 2013).map(lambda car: car['model'])
print(cars.all())