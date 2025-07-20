def bubble_sort(element):

    size = len(element)
    for i in range(size-1):
        for j in range(size-1-i):
            if element[j] > element[j+1]:
                tmp = element[j]
                element[j] = element[j+1]
                element[j+1] = tmp

if __name__=='__main__':

    list = [33,78,2,66,45,22,98,1]
    bubble_sort(list)
    print(list)
