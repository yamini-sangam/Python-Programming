# Given two sets, find the union, intersection, and difference between them

# Function to find the union, intersection, and difference between two sets
def set_operations(set1, set2):
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)
    difference_result1 = set1.difference(set2)
    difference_result2 = set2.difference(set1)

    return union_result, intersection_result, difference_result1, difference_result2


# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform set operations
union_result, intersection_result, difference_result1, difference_result2 = set_operations(set1, set2)

# Print the results
print("Union of the sets:", union_result)
print("Intersection of the sets:", intersection_result)
print("Difference of set1 - set2:", difference_result1)
print("Difference of set2 - set1:", difference_result2)
