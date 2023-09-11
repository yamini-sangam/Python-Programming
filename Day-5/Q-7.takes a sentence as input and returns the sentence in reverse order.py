# Create a function that takes a sentence as input and returns the sentence in reverse order

def reverse_sentence(input_sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = input_sentence.split()

    # Reverse the order of the words
    reversed_words = reversed(words)

    # Join the reversed words to form the reversed sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence
input_sentence = "Hello, World!"
result = reverse_sentence(input_sentence)
print(result)
