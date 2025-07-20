#Implement a function to determine whether a given number is even or odd.

input = int(input('enter the number: '))

def check(n):
    return n % 2 == 0 
result = check(input)


while True:
    if result is True:
        print(f"{input} is even number")
        break
    else:
        print(f"{input} is the odd number")
        break

   
        