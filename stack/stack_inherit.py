from sll import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()
    def push(self, data):
        self.insert_first(data)
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            self.item_count -= 1
            self.delete_first()
            
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return self.item_count
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(30)
s.push(40)
print("peek item", s.peek())
        