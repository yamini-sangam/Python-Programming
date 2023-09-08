# Implement a program that prints the multiplication table of a given number

# Input the number for which you want to generate the multiplication table
number = int(input("Enter a number: "))

# Set the range for the multiplication table (e.g., from 1 to 10)
start = 1
end = 10

# Generate and print the multiplication table
print(f"Multiplication table for {number}:")

for i in range(start, end + 1):
    product = number * i
    print(f"{number} x {i} = {product}")