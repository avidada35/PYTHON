#Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial
"""reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(sentence):
    stack = Stack()
    reversed_sentence = ""
    for char in sentence:
        stack.push(char)
    while not stack.is_empty():
        reversed_sentence += stack.pop()
    return reversed_sentence

# Test the function
sentence = input('enter your sentance: ')
reversed_sentence = reverse_string(sentence)
print(reversed_sentence)
