class Employee:
    '''Создайте класс Employee, у которого будет свойство salary (зарплата). 
    Реализуйте методы для получения и установки значения свойства 
    salary с использованием декоратора @property. 
    Реализуйте также метод для увеличения зарплаты на определенный процент.'''
    def __init__(self, name) -> None:
        self.name = name
        self._salary = None

    @property
    def get_salary(self):
        return self._salary
    
    @get_salary.setter
    def get_salary(self, val):
        if val > 0:
            self._salary = val
        else:
            raise ValueError("don't be negative")
    
    def get_percentage_increase(self, val):
        if val < 0:
            raise ValueError("don't be negative")
        else:
            self.get_PI = (self._salary / 100) * val
            self._salary += self.get_PI
            
        
c1 = Employee('rect')
print(c1.get_salary)
c1.get_salary = 55300
c1.get_percentage_increase(5.12)
print(c1.get_salary)
print(c1.get_PI)