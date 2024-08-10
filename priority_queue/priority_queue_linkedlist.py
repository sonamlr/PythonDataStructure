class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item 
        self.priority = priority
        self.next = next 
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def is_empty(self):
        return self.item_count == 0
    def push(self, data, priority):
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data 
    def size(self):
        return self.item_count
p = PriorityQueue()
p.push("sonam",1)
p.push("gh",4)
p.push("sam",8)
p.push("am",9)
p.push("son",3)
p.push("nam",6)
p.push("onam",2)
p.push("mus", 9)

while not p.is_empty():
    print(p.pop())