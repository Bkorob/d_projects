class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next
# get методы
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
# set методы
    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

class LinkedList: # связанный список
    def __init__(self) -> None:
        self.head = None


    def append(self, data): # добавляет новый узел в связанный список
        new_node = Node(data) # создаем новый объкт узла через класс Node
        curr_node = self.head # начинаем осчёт всегдас головы связанного списка
        if curr_node is None: # если список пуст головой становится наш новый объект
            self.head = new_node 
            return # не забываем вернуть список
        while curr_node.get_next()!= None:  # пока элемент следующий от выбранного не равен Нон
            curr_node = curr_node.get_next() # перемещаем указатель в конец списка
        curr_node.set_next(new_node) # как только условие выполнилось, присваиваем следующему узлу наш объект

    def show(self): # выводим связанный список
        curr_node = self.head # выбираем голову
        output = '' # строка вывода в принт нашего связанного списка
        while curr_node != None: # пока выбранный эл-т не Нан
            output += str(curr_node.get_data()) + '->' # добавляем в строку выбранный эл-т, плюс срелку связи
            curr_node = curr_node.get_next() # перемещаем указатель в конец списка
        print(output) # как только условие выполнилось, принтуем список

    def length(self): # получаем длину списка 
        curr_node = self.head # присваиваем голову указателю
        counter = 0 # заводим счётчик элементов
        while curr_node != None: # пока узел не НАН
            counter += 1 # добавляем к счётчику единицу за текущий узел
            curr_node = curr_node.get_next() # передвигаем указатель вперед
        print(counter) # принтуем значение счётчика

    def push_front(self, data): # добавляем эл-т в начало путем добавления ссылки от него к голове списка
        new_node  = Node(data) # создаем новый узел
        curr_node = self.head # присваиваем указатель голове
        new_node.set_next(curr_node) # связываем ноывй узел с головой 
        self.head = new_node # присваиваем голову новому узлу

    def remove_back(self): # удаляем последний элемент
        curr_node = self.head # присваиваем указателю голову 
        while curr_node.get_next().get_next() != None: # перходим на предпоследний элемент(2метода get_next())
            # нужно для того чтобы разорвать ссылку предпоследнего элемента с последним и тогда он исчезнет
            curr_node = curr_node.get_next() 
        curr_node.set_next(None) # просто удаляем ссылку на него

    def remove_front(self): # удаляем первый эл-т путем разрыва ссылки 
        curr_node = self.head # присваиваем указатель голове
        self.head = curr_node.get_next() # присваиваем голову следующему от указателя элементу
        
    def get_index(self, index): #  находим индекс элемента
        curr_node = self.head # присваиваем голову указателю
        counter = 0 # заводим счётчик 
        while curr_node != None: # пока указатель не на НАН                                           <--
            if counter == index: # доп условие, должно быть до увеличения счётчика, тк индекс мб == 0    |
                return curr_node.get_data() # если индекс == счётчику, возращаем указанный эл-т          |
            curr_node = curr_node.get_next() # двигаем  указатель вперед                              <--
            counter += 1 # добавляем значения счётчику за каждый новый указатель
        raise IndexError('index is out of range') # если индекс за пределами списка, вызываем исключение

    def insert(self, index, data):
        new_node = Node(data)
        curr_node = self.head
        counter = 0
        while curr_node.get_next() != None:
            if index == 0:
                self.push_front(data)
                return
            elif counter + 1  == index: 
                next_curr_item = curr_node.get_next()
                curr_node.set_next(new_node)
                new_node.set_next(next_curr_item)
                return
            counter += 1
            curr_node = curr_node.get_next()
        raise IndexError('Index is out of range')
    
    def remove(self, index):
        curr_node = self.head
        counter = 0
        while curr_node.get_next() != None:
            if index == 0:
                self.remove_front()
                return
            elif counter + 1 == index:
                curr_node.set_next(curr_node.get_next().get_next())
                return
            counter += 1
            curr_node = curr_node.get_next()
        raise IndexError('Index is out of range')
    
    def reverse(self):
        prev = None
        next = None
        curr_node = self.head
        while curr_node != None:
            next = curr_node.get_next()
            curr_node.set_next(prev)
            prev = curr_node
            curr_node = next
        self.head = prev  
            
mylist = LinkedList()

mylist.append(4)
mylist.append(6)
mylist.append(8)
mylist.push_front(12)
# mylist.show()
# mylist.remove_front()
# mylist.show()
# 'https://www.youtube.com/watch?v=xP4G6dR4EBQ'
print(mylist.get_index(2))
mylist.show()
mylist.insert(1,3)
mylist.show()
# mylist.remove(3)
mylist.reverse()
mylist.show()
 

