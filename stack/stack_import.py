from sll import *
class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0
    def is_empty(self):
        return self.is_empty()
    def push(self, data):
        self.mylist.insert_first(data)
        self.item_count += 1
    def pop(self):
        self.mylist.delete_first()
        self.item_count -= 1
    def peek(self):
        return self.mylist.start.item
    def size(self):
        return self.item_count
s = Stack()
s.push(20)
s.push(23)
s.push(25)
print("Size", s.size())
    

    


    