def binary_number(number_list,number_to_find,left_index,right_index):

    if left_index > right_index:
        return -1
    mid_index = (left_index+right_index) // 2
    mid_number = number_list[mid_index]
    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        return binary_number(number_list,number_to_find,mid_index + 1,right_index)
    else:
        return binary_number(number_list,number_to_find,left_index,mid_index -1 ) 

    binary_number(number_list,number_to_find,left_index,right_index)

if __name__ == '__main__':
    list = [33,35,37,233,455,678,6969,789]
    number_tofind = 35

    index = binary_number(list,number_tofind,left_index=0,right_index=len(list) -1)
    print('Number',number_tofind)
    print('index value:',index)


