#  Given a list of names, remove all duplicate names and print the unique names

# Function to remove duplicates from a list of names
def remove_duplicates(names):
    unique_names = list(set(names))
    return unique_names

# Example list of names with duplicates
names_list = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]

# Remove duplicates and get unique names
unique_names = remove_duplicates(names_list)

# Print the unique names
print("Unique Names:")
for name in unique_names:
    print(name)
