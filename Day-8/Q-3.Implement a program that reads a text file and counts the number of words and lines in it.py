# Implement a program that reads a text file and counts the number of words and lines in it

# Function to count the number of words and lines in a text file
def count_words_and_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            lines = text.split('\n')
            words = text.split()

        num_lines = len(lines)
        num_words = len(words)

        return num_lines, num_words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Specify the file path you want to read
file_path = 'sample.txt'  # Replace with the path to your text file

# Call the count_words_and_lines function
result = count_words_and_lines(file_path)

if result is not None:
    num_lines, num_words = result
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
