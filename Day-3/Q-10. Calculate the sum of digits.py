#  Calculate the sum of digits of a given number

# Input the number from the user as a string
number_str = input("Enter a number: ")

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Iterate through each digit character in the number string
for digit_char in number_str:
    # Convert the character back to an integer and add it to the sum
    digit = int(digit_char)
    sum_of_digits += digit

# Display the result
print(f"Sum of digits: {sum_of_digits}")
