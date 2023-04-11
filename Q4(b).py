def shift_left(lst):
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return lst
    # Shift the elements of the list to the left by one position
    shifted_lst = lst[1:] + [lst[0]]
    # Return the shifted list
    return shifted_lst
list1 = [1,2,3]
print(shift_left(list1))
