# Define the list of lists with duplicates
list_of_lists =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Create an empty set to store the unique lists
unique_lists = set()

# Loop through each list in the original list of lists
for lst in list_of_lists:
    # Convert the list to a tuple (because lists are not hashable, but tuples are)
    lst_tuple = tuple(lst)
    # Add the tuple to the set of unique tuples
    unique_lists.add(lst_tuple)

# Convert the set of unique tuples back to a list of lists
unique_list_of_lists = [list(lst_tuple) for lst_tuple in unique_lists]

# Print the original list of lists and the unique list of lists
print("Original List of Lists:")
print(list_of_lists)
print("Unique List of Lists:")
print(unique_list_of_lists)
