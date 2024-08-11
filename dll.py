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
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n 
    def insert_at_last(self, data):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next 
        n = Node(temp, data, None)
        if temp == None:
            self.start = n 
        else:
            temp.next = n
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp 
            temp = temp.next
        return None 
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n 
            temp.next = n 
    def print_all(self):
        temp = self.start 
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next 
    def delete_first(self):
        temp = self.start
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    def delete_last(self):
        temp = self.start 
        if temp is None:
            pass
        elif temp.next is None:
            self.start = None 
        else:
            while temp.next is not None:
                temp = temp.next 
            temp.prev.next = None
    def delete_item(self, data):
        temp = self.start
        if temp is None:
            pass 
        else:
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.prev
                    else:
                        self.start = temp.next 
                    break
                temp = temp.next 
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next 
        return data

        
mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(10), 15)
mylist.delete_first()
mylist.delete_last()
mylist.delete_item(30)
for x in mylist:
    print(x, end=' ')
        



        