#  Implement a function to check if a given year is a leap year or not

# Define a function to check if a year is a leap year
def is_leap_year(year):
    # Leap years are divisible by 4
    # If a year is divisible by 100, it must also be divisible by 400 to be a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year1 = 2000
year2 = 2022

# Check if the years are leap years and print the results
result1 = is_leap_year(year1)
result2 = is_leap_year(year2)

print(f"{year1} is a leap year: {result1}")
print(f"{year2} is a leap year: {result2}")
