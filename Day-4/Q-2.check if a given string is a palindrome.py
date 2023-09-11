# Write a Python function to check if a given string is a palindrome

def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase
    cleaned_string = input_string.replace(" ", "").lower()

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


# Test cases
string1 = "racecar"
string2 = "Hello, World!"
string3 = "A man a plan a canal Panama"

# Check if the strings are palindromes
print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome(string3)}")
