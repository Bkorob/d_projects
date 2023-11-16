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

class LinkedList:
    def __init__(self) -> None:
        self.head = None


    def append(self, data):
        new_node = Node(data)
        curr_node = self.head
        if curr_node is None:
            self.head = new_node
            return
        while curr_node.get_next()!= None:
            curr_node = curr_node.get_next()
        curr_node.set_next(new_node)

    def show(self):
        curr_node = self.head
        output = ''
        while curr_node != None:
            output += str(curr_node.get_data()) + '->'
            curr_node = curr_node.get_next()
        print(output)

    def length(self):
        curr_node = self.head
        counter = 0
        while curr_node != None:
            counter += 1
            curr_node = curr_node.get_next()
        print(counter)

    def push_front(self, data):
        new_node  = Node(data)
        curr_node = self.head
        new_node.set_next(curr_node)
        self.head = new_node

    def remove_back(self): # перходим на предпоследний элемент(2метода get_next())
        curr_node = self.head 
        while curr_node.get_next().get_next() != None:
            curr_node = curr_node.get_next()
        curr_node.set_next(None) # просто удаляем ссылку на него

    def remove_front(self):
        curr_node = self.head
        self.head = curr_node.get_next()

      
mylist = LinkedList()

mylist.append(4)
mylist.append(6)
mylist.append(8)
mylist.show()
mylist.length()
mylist.push_front(12)
mylist.remove_back()
mylist.show()
mylist.remove_front()
mylist.show()
'https://www.youtube.com/watch?v=xP4G6dR4EBQ'