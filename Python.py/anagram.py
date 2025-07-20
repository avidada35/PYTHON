#Create a function to check if two strings are anagrams.
input1 = list(input('enter the 1st word: '))
input2 = list(input('enter the 2nd word: '))

def check(i,x):
    if len(i) == len(x):
        print(f'this two words are the anagramic word \nbecoz the {i} is equal to {x}')
        #build a logic to identify each alphabet of inputs
    else:
        print(f"this is not a anagramic word")

result = check(input1,input2)
print(result)
