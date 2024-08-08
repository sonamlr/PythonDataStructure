class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self):
        self.front = None
        self.rare = None
        self.item_count = 0
    def is_empty(self):
        return self.front == None 
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rare.next = n 
        self.rare = n 
        self.item_count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            self.front = self.front.next
        self.item_count -= 1 
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            return self.front.item
    def get_rare(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            return self.rare.item
    def size(self):
        return self.item_count

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.get_front(), q.get_rare())
q.dequeue()
print(q.get_front(), q.get_rare())
    

        
