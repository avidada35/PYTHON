import random

def passGen():
    print("ready to generate random password")
    length = int(input("Enter the length of the password: "))
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "!@#$%^&*()_+"
    all = lower + upper + number + symbol
    temp = random.sample(all,length)
    password = "".join(temp)
    return password

print(passGen())

