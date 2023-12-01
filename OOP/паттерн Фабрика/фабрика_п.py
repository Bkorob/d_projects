class Animal(): # родительский класс осздается чтобы исключить 
    # отсутствие метода у создаваемого фабрикой класса
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Roar"

class Tiger(Animal):
    def make_sound(self):
        return "Growl"

class Bear(Animal):
    def make_sound(self):
        return "Grr"
    
class AnimalFactory:
    animal_classes = { # словарь служит для диспечеризации вызова классов
        "Lion": Lion,
        "Tiger": Tiger,
        "Bear": Bear
    }

    def create_animal(animal_type):# статик метод(нет self) 
        if animal_type in AnimalFactory.animal_classes:
            return AnimalFactory.animal_classes[animal_type]()# возвращаем класс из словаря, принятому типу. 
        # "()" нужны чтобы класс вызвался.
        else:# вызываем исключение
            raise ValueError("Invalid animal type")
