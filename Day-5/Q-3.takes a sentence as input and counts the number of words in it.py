# Write a program that takes a sentence as input and counts the number of words in it

def count_words(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()

    # Count the number of words
    word_count = len(words)

    return word_count


# Input sentence from the user
input_sentence = input("Enter a sentence: ")

# Call the count_words function to count the words
count = count_words(input_sentence)

# Print the word count
print(f"Number of words in the sentence: {count}")
