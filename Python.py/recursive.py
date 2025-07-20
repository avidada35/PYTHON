#write a recursive func to cal. the sum of first n natural numbers 

def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n

p = sum(5)
print(p)

#write a recursive func to print all the element in a list

cars = ['BMW','AUDI','TATA','MAHINDRA','MG','TOYOTA']

def func(list,index=0):
    if (index == len(list)):
        return  
    print(list[index])
    func(list, index+1)

func(cars)
