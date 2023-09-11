#  Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence

def is_word_in_sentence(sentence, word):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()

    # Check if the word is in the list of words from the sentence
    if word in words:
        return True
    else:
        return False


# Input sentence and word from the user
input_sentence = input("Enter a sentence: ")
input_word = input("Enter a word to check for: ")

# Call the is_word_in_sentence function to check if the word is present in the sentence
result = is_word_in_sentence(input_sentence, input_word)

# Print the result
if result:
    print(f"'{input_word}' is present in the sentence.")
else:
    print(f"'{input_word}' is not present in the sentence.")
