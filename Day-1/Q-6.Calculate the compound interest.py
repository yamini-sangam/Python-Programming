# Calculate the compound interest for a given principal amount, interest rate, and time period

# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, compounding_frequency):
    # Convert the annual interest rate to decimal
    rate_decimal = rate / 100

    # Calculate compound interest
    amount = principal * (1 + (rate_decimal / compounding_frequency)) ** (compounding_frequency * time)
    interest_earned = amount - principal

    return amount, interest_earned


# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, compounding_frequency):
    # Convert the annual interest rate to decimal
    rate_decimal = rate / 100

    # Calculate compound interest
    amount = principal * (1 + (rate_decimal / compounding_frequency)) ** (compounding_frequency * time)
    interest_earned = amount - principal

    return amount, interest_earned


# Input principal amount, annual interest rate, time period, and compounding frequency
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the number of years: "))
compounding_frequency = int(input("Enter the number of times interest is compounded per year: "))

# Calculate compound interest
total_amount, interest = calculate_compound_interest(principal, rate, time, compounding_frequency)

# Display the results
print(f"Principal amount: ${principal:.2f}")
print(f"Annual interest rate: {rate:.2f}%")
print(f"Time period: {time} years")
print(f"Compounding frequency: {compounding_frequency} times per year")
print(f"Total amount after {time} years: ${total_amount:.2f}")
print(f"Interest earned: ${interest:.2f}")
