# Create a Python function to check if a given string is a palindrome

def ispalindrome(s):
    w= ""
    for i in s:
        w= i+w
    return(w)

s="malayalam"
ans=(ispalindrome(s))
if ans==s:
    print("palindrome")
else:
    print("not a palindrome")
