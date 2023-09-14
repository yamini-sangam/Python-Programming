# find the dictionary with the highest value for a specific key

# Function to find the dictionary with the highest value for a specific key
def find_dict_with_highest_value(dict_list, key_to_compare):
    if not dict_list:
        return None

    return max(dict_list, key=lambda x: x.get(key_to_compare, 0))


# Example list of dictionaries
dict_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28}
]

# Key to compare
key_to_compare = 'age'

# Find the dictionary with the highest value for the specified key
result_dict = find_dict_with_highest_value(dict_list, key_to_compare)

# Print the result
print("Dictionary with the highest value for key:", result_dict)
