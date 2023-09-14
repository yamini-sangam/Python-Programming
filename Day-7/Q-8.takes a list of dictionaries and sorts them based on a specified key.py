# Create a function that takes a list of dictionaries and sorts them based on a specified key

# Function to sort a list of dictionaries based on a specified key
def sort_list_of_dicts(list_of_dicts, key_to_sort_by):
    return sorted(list_of_dicts, key=lambda x: x[key_to_sort_by])

# Example list of dictionaries
list_of_dicts = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28}
]

# Key to sort by
key_to_sort_by = 'age'

# Sort the list of dictionaries
sorted_list = sort_list_of_dicts(list_of_dicts, key_to_sort_by)

# Print the sorted list
print("Sorted List of Dicts:")
for entry in sorted_list:
    print(entry)
