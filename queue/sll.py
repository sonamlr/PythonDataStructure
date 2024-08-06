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
        n = Node(data, self.start)
        self.start = n 
    def insert_last(self, data):
        n = Node(data)
        if self.start is None:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n 
    def insert_after(self,temp, data):
        n = Node(data)
        if temp is not None:
            n.next = temp.next 
            temp.next = n
        else:
            raise IndexError("Out of Index")

    def delete_first(self):
        if self.start is None:
            raise IndexError("List is Empty")
        else:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            raise IndexError("List is Empty")
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def delete_item(self, data):
        if self.is_empty():
            pass 
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
            else:
                raise ValueError("Element is not present")
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next 
                
    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp 
                temp = temp.next
    def print_all(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=' ')
                temp = temp.next
    def __iter__(self):
        return SLLInterator(self.start)
class SLLInterator:
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

# s = SLL()
# s.insert_first(10)
# s.insert_first(20)
# s.insert_first(30)
# s.insert_first(40)
# s.insert_first(50)
# print(s.print_all())
# s.delete_first()
# print(s.print_all())
# s.insert_last(60)
# s.insert_last(70)
# s.delete_last()
# s.insert_after((s.search(20)), 15)
# s.delete_item(30)
# print(s.print_all())
# for x in s:
#     print(x, end=' ')

                
