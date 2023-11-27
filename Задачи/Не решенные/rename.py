class People:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
    

class Hello:
    def prints(self, people, nn):
        greers = people(nn)
        print(f'hello, {greers.get_name()}!')


a = Hello()
a.prints(People, '11')