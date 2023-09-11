# Write a function that takes two lists and returns their intersection (common elements)

# Define a function to find the intersection of two lists
def find_intersection(list1, list2):
    # Convert the input lists into sets for efficient membership testing
    set1 = set(list1)
    set2 = set(list2)

    # Use the intersection operator & to find common elements between the sets
    intersection = list(set1 & set2)

    # Return the intersection as a list
    return intersection


# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Call the find_intersection function with the two lists
result = find_intersection(list1, list2)

# Print the original lists and the intersection
print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", result)

