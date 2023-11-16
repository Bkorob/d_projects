class Collection: # каждый метод возвращает новый экземпляр класса.
    def __init__(self, coll):
        self.coll = coll

# принимает ссылку на атрибут класса, проходит по нему функциями и 
# вызывает экземпляр класса с результатом в качестве атрибута 
    def map(self, fn):
        return Collection(list(map(fn, self.coll)))

# каждый раз осздается новый экземпляр, что дает возможность менять коллекции 
# не боясь затронуть результат вызова предыдущей колекции.
    def filter(self, fn):
        return Collection(list(filter(fn, self.coll)))

    # Возвращает саму коллекцию(атрибут класса), а не self.
    # Этот метод всегда последний в цепочке вызовов Collection.
    def all(self):
        return self.coll

cars = Collection([
    {'model': 'rapid', 'year': 2016},
    {'model': 'rio', 'year': 2013},
    {'model': 'mondeo', 'year': 2011},
    {'model': 'octavia', 'year': 2014}
])

filteredCars = cars.filter(lambda car: car['year'] > 2013)
mappedCars = filteredCars.map(lambda car: car['model'])
print(mappedCars.all()) # ['rapid', 'octavia']
print(cars.all())
# [
#   {'model': 'rapid', 'year': 2016},
#   {'model': 'rio', 'year': 2013},
#   {'model': 'mondeo', 'year': 2011},
#   {'model': 'octavia', 'year': 2014}
# ]