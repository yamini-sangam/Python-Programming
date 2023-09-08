#  Create a program that takes a user's name and age as input and prints a greeting message

# Input the user's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check if age is a positive number
if age < 0:
    print("Invalid age. Please enter a positive number.")
else:
    # Print a greeting message based on age
    if age < 18:
        print(f"Hello, {name}! You are a minor.")
    elif age >= 18 and age < 65:
        print(f"Hello, {name}! You are an adult.")
    else:
        print(f"Hello, {name}! You are a senior citizen.")



