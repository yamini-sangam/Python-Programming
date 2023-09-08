#  Given a list of words, count the number of words with more than five characters

# Sample list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Initialize a count variable
count = 0

# Iterate through the list and count words with more than five characters
for word in words:
    if len(word) > 5:
        count += 1

# Display the result
print(f"Number of words with more than five characters: {count}")



