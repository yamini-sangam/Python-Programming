# Given a string, write a function to remove all vowels from it and return the modified string

def remove_vowels(input_string):
    # Define a string containing all lowercase vowels
    vowels = "aeiou"

    # Initialize an empty string to store the modified string
    modified_string = ""

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not a vowel (case-insensitive)
        if char.lower() not in vowels:
            modified_string += char

    return modified_string
input_str = "Hello, World!"
result = remove_vowels(input_str)
print(result)


