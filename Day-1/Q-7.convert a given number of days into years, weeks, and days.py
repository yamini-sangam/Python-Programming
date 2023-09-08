#  Write a program that converts a given number of days into years, weeks, and days

# Input the number of days
total_days = int(input("Enter the number of days: "))

# Calculate years, weeks, and remaining days
years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
days = remaining_days % 7

# Display the result
print(f"{total_days} days is equivalent to:")
print(f"{years} years")
print(f"{weeks} weeks")
print(f"{days} days")

