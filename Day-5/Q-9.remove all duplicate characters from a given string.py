# Write a function to remove all duplicate characters from given string

def remove_duplicates(input_string):
    # Initialize an empty string to store the result
    result = ""

    # Initialize a set to keep track of seen characters
    seen = set()

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not in the set of seen characters
        if char not in seen:
            # Append the character to the result string
            result += char
            # Add the character to the set of seen characters
            seen.add(char)

    return result
input_str = "programming"
result = remove_duplicates(input_str)
print(result)
