# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)

import string

def is_pangram(input_string):
    # Create a set to store the unique lowercase letters in the input string
    alphabet_set = set()

    # Convert the input string to lowercase and iterate through its characters
    for char in input_string.lower():
        # Check if the character is a lowercase letter
        if char.isalpha():
            # Add the letter to the set
            alphabet_set.add(char)

    # Check if the set contains all 26 lowercase letters
    return len(alphabet_set) == 26

# Predefined string to check
predefined_string = "The quick brown fox jumps over the lazy dog"

# Check if the predefined string is a pangram
if is_pangram(predefined_string):
    print("The predefined string is a pangram.")
else:
    print("The predefined string is not a pangram.")
