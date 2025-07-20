#Write a program to print all prime numbers within a given range.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get user input for the range
try:
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
except ValueError:
    print("Invalid input. Please enter valid integers for the range.")
    exit()

# Print prime numbers within the range
print(f"Prime numbers between {start_range} and {end_range}:")
for num in range(start_range, end_range + 1):
    if is_prime(num):
        print(num)
