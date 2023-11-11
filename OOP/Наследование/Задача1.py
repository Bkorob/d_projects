class Fruit:
    '''Создайте класс "Фрукт" и два подкласса "Яблоко" и "Груша". 
    У всех классов должна быть функция "получить_витамины", 
    которая выводит информацию о содержании витаминов во фруктах. 
    Также добавьте методы "указать_цвет" и "указать_форму" для каждого фрукта.'''
    def __init__(self) -> None:
        self.vitamin = 0
    
    def get_vitamin(self):
        print(f'тут {self.vitamin} витаминов')

    def form(self, form):
        print(f'этот фрукт {form}')

    def color(self, col):
        print(f'этот фрукт {col}')


class Apple(Fruit):
    pass


class Penaut(Fruit):
    pass

