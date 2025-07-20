"""Singly Linked List"""

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        return self.start is None
        
    def insert_at_first(self,item):
        D = Node(item)
        if not self.is_empty():
            D.next = self.start
            self.start = D
        self.start = D
        
        
    def delete_at_first(self):
        if not self.is_empty():
            self.start = self.start.next
        return 0
            
    def print(self):
        head = self.start
        while head != None:
            print(head.data,end=' == ')
            head = head.next
        return 0 
        
        
class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0
        
    def push(self,data):
        self.mylist.insert_at_first(data)
        self.item_count += 1
        
    def pop(self):
        if not self.mylist.is_empty():
            self.mylist.delete_at_first()
            self.item_count -= 1
        
    def size(self):
        return self.item_count
        
    def peek(self):
        if not self.mylist.is_empty():
            return self.mylist.start.data
            
        return 0
        


s = Stack()
s.push(10)        
s.push(20)        
s.push(30)        
s.push(40)        
s.push(50)        
print(s.peek())
print()
s.pop()
print(s.peek())

        
        
        
        
        
        
        
        