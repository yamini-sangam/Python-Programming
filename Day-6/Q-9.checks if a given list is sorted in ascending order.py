# Write a program that checks if a given list is sorted in ascending order

# Function to check if a list is sorted in ascending order
def is_sorted_ascending(input_list):
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i + 1]:
            return False
    return True

# Example list to check
sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [3, 1, 4, 2, 5]

# Check if the lists are sorted
if is_sorted_ascending(sorted_list):
    print("The sorted_list is in ascending order.")
else:
    print("The sorted_list is not in ascending order.")

if is_sorted_ascending(unsorted_list):
    print("The unsorted_list is in ascending order.")
else:
    print("The unsorted_list is not in ascending order.")
