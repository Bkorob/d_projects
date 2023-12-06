class Doctor:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.pacients = []

    def add_pacients(self, pacient):
        self.pacients.append(pacient)

    
class Pacient:
    def __init__(self, name) -> None:
        self.name = name

    
class Department:
    def __init__(self, name):
        self.name = name


vasya = Doctor("Vasya", Department('урология'))
print(vasya.department.name)
vasya.add_pacients(Pacient('Xyйло'))
vasya.