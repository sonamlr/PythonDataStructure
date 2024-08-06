class Queue(list):
    def __init__(self):
        self.item_count = 0
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data):
        self.append(data)
        self.item_count += 1
    def dequeue(self):
        if not self.is_empty():
            self.item_count -= 1
            return super().pop(0)
        else:
            raise IndexError("Queue is overflow")
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue is overflow")
    def get_rare(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queue is overflow")
    def size(self):
        return self.item_count
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