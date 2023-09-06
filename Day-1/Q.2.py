#  Create a program that takes a user's name and age as input and prints a greeting message

name= input("Enter your Name: ")
age= int(input("Enter your Age: "))

if (age <0):
    print("Invalid age please enter a positive number")
elif (age< 18):
    print(f"Hello, {name}! You are a minor.")
elif (age>18 and age<65):
    print("Hello "+name+ " your are an adult")
else:
    print("Hello " +name+ "senior citizen")



