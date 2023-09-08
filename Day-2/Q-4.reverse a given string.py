# Create a function to reverse a given string
def reverse_string(input_string):
    # Use slicing to reverse the string
    reversed_str = input_string[::-1]
    return reversed_str

# Input a string from the user
user_input = input("Enter a string: ")

# Call the function to reverse the string
reversed_input = reverse_string(user_input)

# Display the reversed string
print(f"The reversed string is: {reversed_input}")

