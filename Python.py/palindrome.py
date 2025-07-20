#Implement a function to check whether a given string is a palindrome or not.

input = input('ener your word: ')
if input != str(input):
    print('plz enter valid word')
else:
    ()

if list(input) == list(input[::-1]):
    print('YES, this is a palindromic word')
else:
    print(f'this is not a palindromic word \nbecoz the {input} is not equal to reverse of {input}={input[::-1]}')


