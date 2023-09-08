# Create a program that generates the Fibonacci sequence up to a given number of terms

# Function to generate the Fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
        print(fibonacci_sequence)
    return fibonacci_sequence

# Input the number of terms from the user
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(num_terms)

# Display the result
print(f"Fibonacci sequence with {num_terms} terms:")
print(fibonacci_sequence)

