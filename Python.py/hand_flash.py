import random
number1 = random.randrange(2)
number2 = random.randrange(2)
user_no = input('put you hand , black is 0 and white is 1 so flash your hand: ')
user_no3 = int(user_no)
score = 0
comp_score = 0

def program():
    if number1 == number2:
        if (number1,number2) != user_no3:
            print('you win!! becoz computer choses:',number1,",",number2)
    else:
        print('you lose keep again becoz computer number is: ', number1, number2)


program()

