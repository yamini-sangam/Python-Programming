# Implement a function that takes two lists and returns their union (all unique elements from both lists)

# Function to find the union of two lists
def list_union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    union_set = set1.union(set2)
    union_list = list(union_set)
    return union_list

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find the union of the two lists
union_result = list_union(list1, list2)

# Print the union
print("Union of the two lists:", union_result)
