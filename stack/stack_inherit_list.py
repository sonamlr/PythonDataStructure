# stack implementation using list inheriting consept

class Stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self, data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self)
    def insert(self, index, data):
        raise AttributeError("No attribute 'insert' in stack")
s = Stack()
# print("pop item", s.pop())
# print("peek item", s.peek())
print("size", s.size())
s.push(10)
s.push(20)
s.push(30)
s.push(30)
s.push(40)
print("pop item", s.pop())
print("peek item", s.peek())
print("size", s.size())
s.insert(2, 10)

    