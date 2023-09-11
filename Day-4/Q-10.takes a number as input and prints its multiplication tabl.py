#  Create a function that takes a number as input and prints its multiplication table

def multiplication_table(number, range_limit):
    # Iterate through the range and print the multiplication table
    for i in range(1, range_limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage:
number = 7
range_limit = 10

multiplication_table(number, range_limit)
