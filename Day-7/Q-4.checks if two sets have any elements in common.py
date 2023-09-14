# Create a program that checks if two sets have any elements in common

# Function to check if two sets have any elements in common using the intersection() method
def have_common_elements(set1, set2):
    common_elements = set1.intersection(set2)
    return len(common_elements) > 0

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Check if the sets have common elements
if have_common_elements(set1, set2):
    print("The sets have common elements.")
else:
    print("The sets do not have any common elements.")
