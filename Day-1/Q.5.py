# Create a Python function to check if a given string is a palindrome

word= input("Enter a string: ")
cleanword= word.replace(" ", "").lower()
if word == word[::-1]:
    print(word, " is palindrome")
else:
    print(word, " is not a palindrome")
