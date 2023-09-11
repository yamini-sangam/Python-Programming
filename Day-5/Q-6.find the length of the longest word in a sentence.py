# Write a Python program to find the length of the longest word in a sentence

def find_longest_word_length(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()

    # Initialize a variable to keep track of the longest word length
    longest_length = 0

    # Iterate through the words and find the longest length
    for word in words:
        word_length = len(word)
        if word_length > longest_length:
            longest_length = word_length

    return longest_length


# Input sentence from the user
input_sentence = input("Enter a sentence: ")

# Call the find_longest_word_length function to find the length of the longest word
longest_length = find_longest_word_length(input_sentence)

# Print the length of the longest word
print(f"Length of the longest word in the sentence: {longest_length}")
