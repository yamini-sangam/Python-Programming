# Implement a function that checks if a given string is a pangram (contains all letters of the alphabet)

def is_pangram(input_string):
    # Create a set to store unique lowercase letters in the string
    letter_set = set()

    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            letter_set.add(char)

    # Check if the set contains all 26 letters of the alphabet
    return len(letter_set) == 26
input_str1 = "The quick brown fox jumps over the lazy dog"
input_str2 = "Hello, world!"

result1 = is_pangram(input_str1)
result2 = is_pangram(input_str2)

print(f"'{input_str1}' is a pangram: {result1}")
print(f"'{input_str2}' is a pangram: {result2}")
