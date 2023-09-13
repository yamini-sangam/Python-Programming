# Write a Python program to count the occurrences of each element in a given list

# Function to count the occurrences of each element in a list
def count_occurrences(input_list):
    element_count = {}

    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    return element_count

# Example list
input_list = [1, 2, 2, 3, 4, 4, 4, 5]

# Count the occurrences of each element
occurrences = count_occurrences(input_list)

# Print the result
for element, count in occurrences.items():
    print(f"{element}: {count} times")
