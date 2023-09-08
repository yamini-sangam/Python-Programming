# Create a program that takes a sentence as input and counts the number of words in it

# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words using whitespace as the delimiter
words = sentence.split()

# Count the number of words
word_count = len(words)

# Display the result
print(f"The number of words in the sentence is: {word_count}")
