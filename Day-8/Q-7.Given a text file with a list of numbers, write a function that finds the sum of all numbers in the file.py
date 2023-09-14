# Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file

# Function to find the sum of all numbers in a text file
def sum_numbers_in_file(file_path):
    try:
        total_sum = 0

        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())  # Convert each line to a floating-point number
                    total_sum += number
                except ValueError:
                    print(f"Skipping line with non-numeric value: {line.strip()}")

        return total_sum
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Specify the file path with the list of numbers
file_path = 'numbers.txt'  # Replace with the path to your text file

# Call the sum_numbers_in_file function
total = sum_numbers_in_file(file_path)

if total is not None:
    print(f"Sum of all numbers in the file: {total}")
