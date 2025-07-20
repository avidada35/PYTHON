#Generate the Fibonacci sequence up to a specified number of terms.

def fibb(n):
    if n <= 1:
        return n
    else:
        return fibb(n-1) + fibb(n-2)
    

input= int(input('enter the term: '))
for i in range(input):
    print(fibb(i))

