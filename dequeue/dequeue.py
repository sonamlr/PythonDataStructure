class Dequeue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def insert_front(self, data):
        self.items.insert(0, data)
    def insert_rare(self, data):
        self.items.append(data)
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("List is Empty")
    def delete_rare(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("List is Empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("List is Empty")
    def get_rare(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("List is Empty")
    def size(self):
        return len(self.items)

d = Dequeue()
d.insert_front(10)
d.insert_front(20)
d.insert_rare(50)
d.insert_rare(60)
print(d.get_front(), d.get_rare())
d.delete_front()
d.delete_rare()
print(d.get_front(), d.get_rare())