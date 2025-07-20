
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
        
    def delete_at_last(self):
        if not self.is_empty():
            if self.start.next is None:
                self.start = None
            else:
                head = self.start
                while head.next.next != None:
                    head = head.next
                head.next = None
            
    def head_display(self):
        head = self.start
        while head.next != None:
            head = head.next
        return head.data
        
        
            
class Queue:
    
    def __init__(self):
        self.list = SLL()
        self.data_count = 0
        
        
    def is_empty(self):
        return self.list.is_empty()
    
    def push(self,data):
        self.list.insert_at_first(data)
        self.data_count += 1
        
    def pop(self):
        if not self.is_empty():
            self.list.delete_at_last()
            self.data_count -= 1
        return 0
        
    def get_front(self):
        if not self.is_empty():
            return self.list.head_display()
        return None
        
    def get_rear(self):
        if not self.is_empty():
            return self.list.start.data
        return None
        
    def size(self):
        return self.data_count
        

q = Queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.push(60)
print(q.get_front())
print(q.get_rear())

        
#O/P = 10
#      60