# Create a Python function to check if a given string is a palindrome

def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for case-insensitive comparison
    cleaned_string = input_string.replace(" ", "").lower()

    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]


# Input a string from the user
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
