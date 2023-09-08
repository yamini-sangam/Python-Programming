#  Given a list of integers, find all the even numbers and store them in a new list

# Sample list of integers
numbers = [12, 45, 7, 23, 56, 9, 1, 78, 34]

# Initialize a new list to store even numbers
even_numbers = []

# Iterate through the list and check for even numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# Display the even numbers
print("Even numbers in the list:", even_numbers)
