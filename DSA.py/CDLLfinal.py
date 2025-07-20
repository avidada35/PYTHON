"""Circular Doubly Linked List"""

class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next
        
class CDLL:
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        return self.start is None
        
    def insert_at_start(self,data):
        if self.is_empty():
            D = Node(data=data)
            self.start = D
            self.start.next = self.start
            self.start.prev = self.start
            
        else:
            D = Node(self.start.prev,data,self.start)
            self.start.prev.next = D
            self.start.prev = D
            self.start = D
            
    def insert_at_end(self,data):
        if self.is_empty():
            D = Node(data=data)
            self.start = D
            self.start.next = self.start
            self.start.prev = self.start
        else:
            D = Node(self.start.prev,data,self.start)
            self.start.prev.next = D
            self.start.prev = D
            
    def search(self,item):
        head = self.start 
        while True:
            if head.data == item:
                print(f"{head.data} is Found!!")
            head = head.next
            if head == self.start:
                break
            
    def insert_after(self,after_val,data):
        if self.is_empty():
            head = self.start
            while head.data != after_val:
                head = head.next
            D = Node(head,data,head.next)
            head.next = D
            head.next.prev = D
        
    def delete_first(self):
        self.start.next.prev = self.start.prev
        self.start.prev.next = self.start.next
        self.start = self.start.next
        
    def delete_last(self):
        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev
        
        
    def delete(self,item):
        head = self.start
        while head.data != item:
            head = head.next
        head.next.prev = head.prev
        head.prev.next = head.next
        
        
    def print(self):
        head = self.start
        while True:
            print(head.data,end=" == ")
            head = head.next
            if head == self.start:
                break
        
cdll = CDLL()
cdll.insert_at_start(5)
cdll.insert_at_start(10)
cdll.insert_at_start(20)
cdll.insert_at_start(35)
cdll.insert_at_end(55)
cdll.insert_at_end(88)
#cdll.search(5)
cdll.insert_after(10,11)
cdll.insert_after(55,69)
cdll.insert_after(88,100)
cdll.insert_after(35,40)
cdll.print()
print()
cdll.delete_first()
cdll.print()
print()
cdll.delete(55)
cdll.print()
            
            
            
            
            
            
            
        