""" Queue in List Method"""

class Queue:
    def __init__(self):
        self.list = []
        
    def is_empty(self):
        return len(self.list) == 0
        
    def enqueue(self,data):
        self.list.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            self.list.pop(0)
        return 0 
        
        
    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        return 0 
        
        
    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        return 0 
        
    def size(self):
        return len(self.list)
        
    
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.get_front())
print()
print(q.get_rear())
    
    
    
    
    
    
    
    
    
    
    
        
    