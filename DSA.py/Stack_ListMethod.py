"""STACK"""

class Stack:
    def __init__(self):
        self.data = []
        
    def is_empty(self):
        return len(self.data) == 0
        
    def push(self,item):
        self.data.append(item)
            
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError('Stack is Empty!!')
            
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError('Stack is Empty!!')
            
    def size(self):
        return len(self.data)
        
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print()
print(s1.size())
print(s1.pop())
print(s1.peek())
print()
print(s1.size())