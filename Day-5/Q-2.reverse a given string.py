# Create a function to reverse a given string

def reverse_string(input_string):
    # Initialize an empty string to store the reversed string
    reversed_str = ""

    # Iterate through the input string in reverse order
    for char in reversed(input_string):
        # Append each character to the reversed string
        reversed_str += char

    return reversed_str


# Example usage:
input_str = "Hello, World!"
reversed_result = reverse_string(input_str)
print("Original String:", input_str)
print("Reversed String:", reversed_result)
