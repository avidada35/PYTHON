"""Bubble Sorting"""
def sorting(L):
    for i in range(1,len(L)):
        for j in range(len(L)-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
            
L = [26,58,43,67,92,11]
sorting(L)          
print(L)
#output : [11, 26, 43, 58, 67, 92]

    