# Given a list of words, concatenate them into a single string separated by spaces

def concatenate_words(words):
    # Use the join() method to concatenate the words with spaces
    concatenated_string = ' '.join(words)
    return concatenated_string
word_list = ["Hello", "world", "this", "is", "a", "concatenation", "example"]
result = concatenate_words(word_list)
print(result)
