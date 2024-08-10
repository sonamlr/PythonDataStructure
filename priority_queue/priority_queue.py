class PriorityQueue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, data, priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<= priority:
            index += 1

        self.items.insert(index, (data, priority))
    def size(self):
        return len(self.items)
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("Priority Queue is Empty")

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
