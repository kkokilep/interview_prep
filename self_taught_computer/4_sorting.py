

def bubble_sort(a_list):
    list_length = len(a_list) - 1

    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list

def bubble_sort_more_efficient(a_list):
    list_length = len(a_list) - 1

    for i in range(list_length):
        for j in range(list_length-i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list

def bubble_sort_no_swaps(a_list):
    list_length = len(a_list) - 1

    for i in range(list_length):
        no_swaps = True
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
            if(no_swaps):
                return a_list
    return a_list

def insertion_sort(a_list):
    for i in range(1,len(a_list)):
        value = a_list[i]
        while(i>0 and a_list[i-1]>value):
            a_list[i] = a_list[i-1]
            i = i - 1
        a_list[i] = value
    return a_list

def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
    left_ind = 0
    right_ind = 0
    alist_ind = 0
    while left_ind < len(left_half) and right_ind < len(right_half):
        if (left_half[left_ind] <= right_half[right_ind]):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
        else:
            a_list[alist_ind] = right_half[right_ind]
        alist_ind += 1
    while left_ind < len(left_half):
        a_list[alist_ind] = left_half[left_ind]
        left_ind += 1
        alist_ind += 1
    while right_ind < len(right_half):
        a_list[alist_ind] = right_half[right_ind]
        right_ind += 1
        alist_ind += 1