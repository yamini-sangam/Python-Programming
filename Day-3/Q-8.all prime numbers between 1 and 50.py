# Create a loop that prints all prime numbers between 1 and 50

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

# Loop to print prime numbers between 1 and 50
print("Prime numbers between 1 and 50:")
for number in range(1, 51):
    if is_prime(number):
        print(number)
