def count_vowels(input_string):
    # Define a list of vowels
    vowels = "AEIOUaeiou"

    # Initialize a count variable to store the count of vowels
    count = 0

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            count += 1

    return count

# Example usage:
input_string = input("Enter a string: ")
result = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {result}")
