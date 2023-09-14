# Write a Python program that counts the number of occurrences of each character in a given string using a dictionary

# Function to count the occurrences of each character in a string
def count_characters(input_string):
    character_count = {}

    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count


# Example string
input_string = "hello world"

# Count the occurrences of each character
character_counts = count_characters(input_string)

# Print the result
print("Character Counts:")
for char, count in character_counts.items():
    print(f"'{char}': {count} times")
