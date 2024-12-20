import array

def create_array():
    arr = array.array('f',(1.0,1.5,2.0,2.5))
    return arr

def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if(zero_index != index):
                a_list[index] = 0
            zero_index = zero_index + 1
    return (a_list)

def return_duplicates(a_list):
    dups = []
    a_set = set()
    for item in a_list:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if(l1 == l2):
            dups.append(item)
    return dups

def return_intersection(list1, list2):
    list3 = [v for v in list1 if v in list2]
    return list3

def return_iter(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

