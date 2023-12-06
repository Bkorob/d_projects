class Parent: # родительский класс с определенными в нем методами
    def __init__(self) -> None:
        self.val = 0

    def inc(self):
        self.val+=1

    def dec(self):
        self.val-=1

    def get(self):
        return self.val
        
class Child(Parent): #класс наследник. имеет все методы родителя по умолчанию.
    # если мы хотим переопределить метод в наследнике то просто переписываем его
    # если хотим оставить и функционал родителя и добавить чтото от себя 
    # используем метод super() с у указанием переопределяемого родительского метода
    
    def inc(self):
        super().inc()
        return f'{super().get()} столько'
        

# # gr = Parent()
# # gr.inc()
# # print(gr.get())
c = Child()

c.inc()
c.inc()
print(c.inc())

