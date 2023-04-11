def count_occurrences(lst):
    # Create an empty dictionary to store the count of each element
    count_dict = {}
    # Loop through each element in the list
    for elem in lst:
        # If the element is already in the dictionary, increment its count
        if elem in count_dict:
            count_dict[elem] += 1
        # Otherwise, add the element to the dictionary with a count of 1
        else:
            count_dict[elem] = 1
    # Return the dictionary of element counts
    return count_dict
list1 =[11, 45, 8, 11, 23, 45, 23, 45, 89, 11, 89] 
print(count_occurrences(list1))
