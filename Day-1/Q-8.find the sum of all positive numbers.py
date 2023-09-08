# Given a list of integers, find the sum of all positive numbers

# Sample list of integers
numbers = [-2, 3, 7, -1, 8, -5, 12]

# Initialize a variable to store the sum
positive_sum = 0

# Iterate through the list and add positive numbers to the sum
for num in numbers:
    if num > 0:
        positive_sum += num

# Display the result
print(f"The sum of all positive numbers in the list is: {positive_sum}")




