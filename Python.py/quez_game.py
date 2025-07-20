
start = input("do you want to solve quez game: ")
if start != 'yes':
    print('you should try once a time')


print('okay lets play')



score = 0

ans_1 = input('What is the capital of India? ')
if ans_1 == 'dilli':
        print('correct!')
        score += 1
else:
    print('incorrect!!')
    

ans_2 = input('Who is the current Prime Minister of India? ')
if ans_2 == 'modi':
     print('correct!!')
else:
     print('incorrect!!')
     score += 1
        
ans_3 = input('What is the currency of India?')
if ans_3 == 'Rupee':
    print('correct!')
    score += 1
else:
    print('incorrect!!')
    
ans_4 = input('When was India independence day? ')
if ans_4 == '15 August':
    print('correct!')
    score += 1
else:
    print('incorrect!!')


print('your score is: '+str((score/4)*100)) 

    

          

    



