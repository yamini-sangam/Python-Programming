# Implement a program that swaps the values of two variable

# Input two values from the user
value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")

# Print the original values
print(f"Original values: value1 = {value1}, value2 = {value2}")

# Swap the values using a temporary variable
temp = value1
value1 = value2
value2 = temp

# Print the swapped values
print(f"Swapped values: value1 = {value1}, value2 = {value2}")

