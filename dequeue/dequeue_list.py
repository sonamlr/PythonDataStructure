class Dequeue(list):
    def __init__(self):
        super().__init__()
    def is_empty(self):
        return len(self) == 0
    def insert_front(self, data):
        super().insert(0, data)
    def insert_rare(self, data):
        super().append(data)
    def get_front(self):
        if not self.is_empty():
            return self[0]
    def get_rare(self):
        if not self.is_empty():
            return self[-1]
    def delete_front(self):
        if not self.is_empty():
            super().pop(0)
    def delete_rare(self):
        if not self.is_empty():
            super().pop(-1)
    def size(self):
        return len(self)
d = Dequeue()
d.insert_front(10)
d.insert_front(20)
d.insert_rare(50)
d.insert_rare(60)
print(d.get_front(), d.get_rare())
d.delete_front()
d.delete_rare()
print(d.get_front(), d.get_rare())
print(d.size())
