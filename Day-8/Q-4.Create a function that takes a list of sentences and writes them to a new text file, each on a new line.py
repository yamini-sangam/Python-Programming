# Create a function that takes a list of sentences and writes them to a new text file, each on a new line

# Function to write a list of sentences to a text file, one sentence per line
def write_sentences_to_file(sentences, file_path):
    try:
        with open(file_path, 'w') as file:
            for sentence in sentences:
                file.write(sentence + '\n')
        print(f"Sentences written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example list of sentences
sentences = [
    "This is the first sentence.",
    "Here is another sentence.",
    "And one more sentence for the example."
]

# Specify the file path where you want to save the sentences
file_path = 'sentences.txt'  # Replace with the desired file path

# Call the write_sentences_to_file function
write_sentences_to_file(sentences, file_path)
