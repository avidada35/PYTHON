"""Recursion Function"""

# 1) print first N natural numbers

def func(n):
    if n <= 0:
        return
    func(n-1)
    print(n,end=" ")
    
func(10)
# O/P = 1 2 3 4 5 6 7 8 9 10 
print()
# 2) print first N natural numbers in reverse order

def func(n):
    if n<=0:
        return 
    print(n,end=" ")
    func(n-1)
    
func(10)
# O/P 10 9 8 7 6 5 4 3 2 1
print()
# 3) print first N'th ODD numbers

def func(n):
    if n > 0:
        func(n-1)
        print(2*n-1,end=" ")
        
func(5)
# O/P 1 3 5 7 9
print()

# 4) Print First N'th Even Number

def func(n):
    if n>0:
        func(n-1)
        print(n*2,end=" ")
        
func(5)
# O/P 2 4 6 8 10
print()
# 5) print first N'th odd number in revere order
def func(n):
    if n>0:
        print(n*2-1,end=" ")
        func(n-1)
func(5)
# O/P 9 7 5 3 1
print()
# 6) Print First N'th Even Number

def func(n):
    if n>0:
        print(n*2,end=" ")
        func(n-1)
func(5)
# O/P 10 8 6 4 2 
print()
# 7) Sum of first N'th number
def func(n):
    if n != 0:
        return n + func(n-1)
    return 0

print(func(5))
# O/P 15
print()
# 8) sum of first N odd numbers
def func(n):
    if n != 0:
        return 2*n-1 + func(n-1)
    return 0 
print(func(5))
# O/P 25
print()
# 9) sum of first N evev numbers
def func(n):
    if n != 0:
        return 2*n + func(n-1)
    return 0 
print(func(5))
# O/P 30
print()
# 10) Factorial
def func(n):
    if n != 0:
        return n * func(n-1)
    return 1
print(func(5))
# O/P 120
print()
# 11) sum of first N numbers square
def func(n):
    if n != 1:
        return n**2 + func(n-1)
    return 1
print(func(10))
# O/P 385


    



    
    
    
    
    
    





