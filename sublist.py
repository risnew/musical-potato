
list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = [1,5,3,7]
list_3 = [9,3,4,5,6,7,1,2]

def is_sublist(sub_list, list):
    new_list = []
    for i in sub_list:
        if i in list:
            new_list.append(i)
    if new_list == sub_list:
        return True
    else:
        return False


print("Expected False -", is_sublist(list_1, list_2))
print("Expected True -", is_sublist(list_3, list_3))
print("Expected True -", is_sublist(list_2, list_1))
print("Expected True -", is_sublist(list_3, list_1))
