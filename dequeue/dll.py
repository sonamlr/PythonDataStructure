class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev 
        self.item = item 
        self.next = next 

class DLL:
    def __init__(self, start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_start(self, data):
        n = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n 
    def insert_last(self, data):
        n = Node(None, data, None)
        if self.start is None:
            n.next = self.start
            self.start = n
        elif self.start.next is None:
            n.prev = self.start
            self.start.next = n 
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n.prev = temp
            temp.next = n
    def search(self,data):
        if data is not None:
            pass
    def insert_after(self, temp, data):
        pass

    def delete_start(self):
        if self.start is None:
            raise IndexError("List is Empty")
        elif self.start.next is None:
            self.start = None 
        else:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            raise IndexError("List is Empty")
        elif self.start.next is None:
            self.start = None 
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next 
            temp.prev.next = None
    def print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
d = DLL()
d.insert_start(10)
d.insert_start(20)
d.insert_start(30)
d.insert_start(40)
d.delete_start()
d.insert_last(90)
d.insert_last(60)
d.insert_last(50)
d.delete_last()
d.print_all()
        
