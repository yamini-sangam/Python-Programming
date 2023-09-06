# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)

import string
def check_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False
    return True

s = "the quick brown fox jumps over the lazy dog"
if check_pangram(s) == True:
    print("Yes")
else:
    print("No")