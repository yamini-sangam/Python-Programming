# Given a list of numbers, create a function to find the sum of all positive numbers

def sum_positive_numbers(numbers):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list
    for number in numbers:
        # Check if the number is positive
        if number > 0:
            total += number

    return total

# Example list of numbers
numbers_list = [1, -2, 3, 4, -5, 6, 7, -8]

# Call the function to find the sum of positive numbers
result = sum_positive_numbers(numbers_list)

# Display the result
print(f"Sum of positive numbers: {result}")
