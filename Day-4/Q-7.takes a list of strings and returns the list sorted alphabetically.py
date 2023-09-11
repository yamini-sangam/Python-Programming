# Create a function that takes a list of strings and returns the list sorted alphabetically

def sort_strings_alphabetically(string_list):
    sorted_list = sorted(string_list)
    return sorted_list

# Example usage:
my_list = ["banana", "apple", "cherry", "date"]
result = sort_strings_alphabetically(my_list)
print("Original List:", my_list)
print("Sorted List:", result)
