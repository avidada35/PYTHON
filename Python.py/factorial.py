#Write a function to calculate the factorial of a given no.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    


# Example usage:

number = int(input('enter the number: '))
result = factorial(number)
print(f"The factorial of {number} is: {result}")




        
    



    
    





    
