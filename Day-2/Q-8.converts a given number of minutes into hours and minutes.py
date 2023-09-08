# Implement a program that converts a given number of minutes into hours and minutes

# Get the input from the user
minutes = int(input("Enter the number of minutes: "))

# Calculate the hours and remaining minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# Display the result
print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")