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
            
    def print(self):
        head = self.start
        while True:
            print(head.data,end="<--")
            head = head.next
            if head == self.start:
                break
        
cdll = CDLL()
cdll.insert_at_start(5)
cdll.insert_at_start(10)
cdll.insert_at_start(20)
cdll.insert_at_start(35)
cdll.print()
print()
            
            
            
            
            
            
            
        