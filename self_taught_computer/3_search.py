from bisect import bisect_left
# https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
def linear_search(a_list,n):
    for i in a_list:
        if i == n:
            return True
    return False

def binary_search(a_list,n):
    first = 0
    last = len(a_list)-1
    while last >= first:
        mid = (first + last)//2
        if(a_list[mid] == n):
            return True
        else:
            if(n<a_list[mid]):
                last = mid-1
            else:
                first = mid+1
    return False

def binary_search_bisect(a_list,n):
    index = bisect_left(a_list,n)
    if index <= len(a_list) and a_list[index] == n:
        return True
    return False