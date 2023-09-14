# Implement a function that takes a list of strings and returns a set of unique characters present in all strings

# Function to find unique characters present in all strings in a list
def unique_characters_in_all_strings(string_list):
    if not string_list:
        return set()  # Return an empty set if the input list is empty

    # Initialize a set with characters from the first string
    common_characters = set(string_list[0])

    # Iterate through the rest of the strings
    for string in string_list[1:]:
        # Find the set of characters in the current string
        current_characters = set(string)

        # Update the common_characters set with the intersection of characters
        common_characters.intersection_update(current_characters)

    return common_characters


# Example list of strings
string_list = ["apple", "banana", "cherry", "date"]

# Find unique characters present in all strings
unique_chars = unique_characters_in_all_strings(string_list)

# Print the result
print("Unique characters present in all strings:", unique_chars)

