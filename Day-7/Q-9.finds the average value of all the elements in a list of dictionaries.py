# Write a program that finds the average value of all the elements in a list of dictionaries

# Function to find the average value of all elements in a list of dictionaries
def average_value_of_dicts_list(list_of_dicts):
    total_sum = 0
    total_count = 0

    for dictionary in list_of_dicts:
        for value in dictionary.values():
            if isinstance(value, (int, float)):
                total_sum += value
                total_count += 1

    if total_count == 0:
        return 0  # To avoid division by zero if there are no numeric values

    average = total_sum / total_count
    return average

# Example list of dictionaries
list_of_dicts = [
    {'value1': 10, 'value2': 20, 'value3': 30},
    {'value1': 5, 'value2': 15},
    {'value1': 25, 'value2': 35, 'value3': 45},
]

# Find the average value
average = average_value_of_dicts_list(list_of_dicts)

# Print the average value
print("Average value of all elements:", average)
