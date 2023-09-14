# Write a program that finds the most frequent element in a list

# Function to find the most frequent element in a list
def most_frequent_element(input_list):
    frequency_dict = {}

    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    # Find the element with the highest frequency
    most_frequent = max(frequency_dict, key=frequency_dict.get)
    frequency = frequency_dict[most_frequent]

    return most_frequent, frequency


# Example list
input_list = [1, 2, 2, 3, 4, 4, 4, 5]

# Find the most frequent element
most_frequent, frequency = most_frequent_element(input_list)

# Print the result
print(f"The most frequent element is {most_frequent} with a frequency of {frequency} times.")
