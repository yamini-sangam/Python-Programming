# Write a program that calculates the factorial of a given number

# Input the number for which you want to calculate the factorial
number = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate the factorial for positive numbers
    for i in range(1, number + 1):
        factorial *= i

    # Display the result
    print(f"The factorial of {number} is {factorial}")
