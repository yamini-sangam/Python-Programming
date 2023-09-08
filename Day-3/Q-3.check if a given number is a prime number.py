# Write a Python program to check if a given number is a prime number

def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    elif num <= 3:
        return True   # 2 and 3 are prime
    elif num % 2 == 0 or num % 3 == 0:
        return False  # Multiples of 2 and 3 are not prime
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False  # If divisible by any number from i to i+2, it's not prime
            i += 6  # Check factors in increments of 6

        return True  # If no factors found, it's prime

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is prime using the is_prime function
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
