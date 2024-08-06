class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is overflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is overflow")
    def get_rare(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is overflow")
    def size(self):
        return len(self.items)
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
try:
    print("size ",q.size())
    print("dequeue ",q.dequeue())
    print("Front ",q.get_front())
    print("Rare ",q.get_rare())
except IndexError as e:
    print(e)


    
