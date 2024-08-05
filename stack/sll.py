class Node:
    def __init__(self, item=None, next=None):
        self.item = item 
        self.next = next 
class SLL:
    def __init__(self, start=None):
        self.start = start 
    def is_empty(self):
        return self.start == None 
    def insert_first(self, data):
        n = Node(data,self.start)
        self.start = n
    def insert_last(self, data):
        n = Node(data)
        temp = self.start
        if not self.is_empty():
            while temp is not None:
                temp = temp.next
            temp = n
        else:
            self.start = n
    def search(self,data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp 
                temp = temp.next 
        else:
            return None 
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
    def print_all(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=' ')
                temp = temp.next 
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next 
    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                temp = temp.next
            temp = None
        else:
            pass
    def delete_after(self, data):
        if self.is_empty():
            pass
        else: 
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    temp = temp.next 
                    break
                temp = temp.next
    def __iter__(self):
        return SLLItertor(self.start)
class SLLItertor:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


                

        


