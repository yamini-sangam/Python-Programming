# Implement a function that removes a key-value pair from a dictionary

# Function to remove a key-value pair from a dictionary using del
def remove_key_value_pair(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Remove a key-value pair
remove_key_value_pair(my_dict, 'b')

# Print the modified dictionary
print("Modified Dictionary:")
print(my_dict)
