# Implement a function that returns the factorial of a given number using recursion

def factorial_recursive(number):
    # Base case: Factorial of 0 is 1
    if number == 0:
        return 1
    # Recursive case: Factorial of n is n multiplied by factorial of (n-1)
    else:
        return number * factorial_recursive(number - 1)

# Test the function with an example
num = 5
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")
