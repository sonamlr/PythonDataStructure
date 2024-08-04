# stack implementation
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Poped item", s.pop())
print("Peek item", s.peek())
s.push(50)
print("Poped item", s.pop())
print("Poped item", s.pop())
s.push(60)
print("Size :", s.size())
    
        