list = [2200,2350,2600,2130,2190]
#       jan  feb  mar  apr june
#        0    1    2    3   4

#In Feb, how many dollars you spent extra compare to January?

spent = list[1] - list[0]

print('extra dollars spent in feb is,',spent)
print()

#Find out your total expense in first quarter (first three months) of the year.

total = list[0]+list[1]+list[2]
print('Toatal expence in first quater is,',total)
print()

#3. Find out if you spent exactly 2000 dollars in any month

check = 2000 in list
print(check)
print()

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

list.append(1980)
print('new mounth val. is,',list)
print()

'''5. You returned an item that you bought in a month of April and got a refund of 200. 
Make a correction to your monthly expense list
based on this'''

list[-2]= list[-2] - 200

print('updated val. in apr is,',list)







