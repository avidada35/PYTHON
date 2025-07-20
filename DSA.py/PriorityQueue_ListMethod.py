"""Priority Queue using List"""

class PriorityQueue:
    def __init__(self,list=None,priority=None):
        self.list = []
        self.priority = priority
        
    def is_empty(self):
        return len(self.data) == None
        
    def push(self,item,priority):
        index = 0 
        while index < len(self.list) and self.list[index][1] <= priority:
            index += 1
        self.list.insert(index,(list,priority))
        
    def pop(self):
        if not self.is_empty():
            self.list.pop(0)[0]
        return 0 
        
    def size(self):
        return len(self.list)


pq = PriorityQueue()
pq.push(10,2)
pq.push(20,5)
pq.push(30,6)
pq.push(40,23)
pq.push(50,55)
pq.push(60,88)
pq.push(70,3)
print(pq.pop())
            
   