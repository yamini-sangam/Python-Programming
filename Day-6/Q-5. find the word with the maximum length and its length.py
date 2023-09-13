# Given a list of words, find the word with the maximum length and its length

# Function to find the word with the maximum length and its length
def find_max_length_word(words):
    if not words:
        return None, 0

    max_length_word = words[0]
    max_length = len(max_length_word)

    for word in words:
        current_length = len(word)
        if current_length > max_length:
            max_length_word = word
            max_length = current_length

    return max_length_word, max_length


# Example list of words
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Find the word with the maximum length and its length
max_length_word, max_length = find_max_length_word(word_list)

# Print the result
print("Word with maximum length:", max_length_word)
print("Length of maximum length word:", max_length)
