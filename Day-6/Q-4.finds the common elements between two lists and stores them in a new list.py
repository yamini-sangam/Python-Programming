#  Create a program that finds the common elements between two lists and stores them in a new list

# Function to find common elements between two lists
def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find common elements
common_elements = find_common_elements(list1, list2)

# Print the common elements
print("Common elements:", common_elements)
