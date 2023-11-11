class Cat:
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    @property
    def get_breed(self):
        self.breed = f'{self.name[-2:]}{self.sex[0]}{self.age}'
        return self.breed
    # сеттре служит для изменения значения атрибута, возращаемого
    # геттером
    @get_breed.setter
    # название совпадает с геттером, чтобы можно было менять его
    # как атрибут. ВАЖНО!: СЕТТЕР МОЖЕТ ПРИНЯТЬ ТОЛЬКО ОДИН АРГУМЕНТ ДЛЯ ИЗМЕНЕНИЯ, ну или кортеж))
    def get_breed(self, new_breed):#принимает новое значение
        self.name, self.age, self.sex = new_breed.split(' ')
    # Ничего не возращает в отличии от gettera

cat1 = Cat('Myrka', 10, 'female')
cat2 = Cat('Motya', 11, 'male')
print(cat1.get_breed)
print(cat2.get_breed)
#  заменяем атрибут get_breed, который на самом деле метод)
cat1.get_breed = 'aaa ccc 111'
print(cat1.get_breed)
