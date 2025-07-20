"""Circular Linked List"""

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next 
        
class CLL:
    def __init__(self):
        self.last = None
        
    def Is_Empty(self):
        return self.last is None
        
    def Insert_At_Start(self,data):
        D = Node(data)
        if self.last == None:
            self.last = D
            D.next = self.last
        else:
            D.next = self.last.next
            self.last.next = D
            
    def Insert_At_Last(self,data):
        D = Node(data)
        if self.last is None:
            self.last == D
            D.next = self.last
        else:
            D.next = self.last.next
            self.last.next = D
            self.last == D
            
    def search(self,item):
        head = self.last.next
        while head == self.last.next:
            if head.data == item:
                print('Found!!')
            head = head.next
        print('Not Found!!')
            
    def Print(self):
        head = self.last.next
        while True:
            print(head.data,end="<--")
            head = head.next
            if head == self.last.next:
                break
        
S=CLL()
S.Insert_At_Start(10)
S.Insert_At_Start(20)
S.Insert_At_Start(35)
S.Insert_At_Last(5)
S.search(35)
S.Print()
        
        
        
        
        