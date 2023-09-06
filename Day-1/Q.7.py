#  Write a program that converts a given number of days into years, weeks, and days

total_days= int(input("Enter days: "))


years = int(total_days // 365)
print(years)
remaining_days= total_days-(years*365)
weeks = int(remaining_days // 7)
print(weeks)
days = remaining_days % 7
print(days)