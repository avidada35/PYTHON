def insertion_sort(element):
    for i in range(1,len(element)):
        anchor = element[i]
        j = i-1

        while j >= 0 and anchor < element[j]:
            element[j+1] = element[j]
            j = j - 1 
        element[j+1] = anchor

element = [33,55,2,3,89,69,32,1,333]
insertion_sort(element)
print(element)

