def swap(a,b,arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(element,start,end):
    if start < end:
        pi = partition(element,start,end)
        quick_sort(element,start,pi-1)
        quick_sort(element,pi+1,end)

def partition(element,start,end):

    pivot = element[start]

    while start<end:
        while start<len(element) and element[start] <= pivot:
            start +=1

        while element[end] > pivot:
            end -= 1

        if start < end:
            swap(start,end,element)
    
    swap(pivot,end,element)

    return end

if __name__ == '__main__':

    element = [1,77,45,66,3,999,65,12,334,0]
    quick_sort(element,0,len(element)-1)
    print(element)