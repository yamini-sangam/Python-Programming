# Given two dictionaries, merge them into a single dictionary

# Function to merge two dictionaries using the update() method
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge the dictionaries
merged_result = merge_dictionaries(dict1, dict2)

# Print the merged dictionary
print("Merged Dictionary:")
print(merged_result)
