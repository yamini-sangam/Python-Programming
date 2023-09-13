#  Create a function that takes a list of strings and returns the list sorted by the length of the strings

# Function to sort a list of strings by their length
def sort_by_length(strings):
    return sorted(strings, key=len)

# Example list of strings
string_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Sort the list by string length
sorted_list = sort_by_length(string_list)

# Print the sorted list
print("Sorted by length:")
for string in sorted_list:
    print(string)
