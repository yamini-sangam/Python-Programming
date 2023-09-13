# Implement a function that takes a list of numbers and returns a new list with the squared values

def square_list(numbers):
    squared_values = []  # Create an empty list to store squared values
    for num in numbers:
        squared_values.append(num ** 2)  # Square each number and append it to the new list
    return squared_values

# Example usage:
original_list = [1, 2, 3, 4, 5]
squared_list = square_list(original_list)
print(squared_list)
