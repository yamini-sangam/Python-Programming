# Given a list of numbers, find the maximum and minimum values

numbers= input("Enter numbers separated by commas: ")
list= [int(x) for x in numbers.split(',')]

if not list:
    print("Empty list")
else:
    min_val = max_val = list[0]
for num in list:
    if num> max_val:
        max_val=num
    elif num<min_val:
        min_val=num
print("Maximum value in list is: " + str(max_val))
print("Minimum value in list is: " + str(min_val))
