# Given a list of integers, find the sum of all positive numbers

numbers= input("Enter numbers separated by commas: ")
list= [int(x) for x in numbers.split(',')]
sum=0
for x in list:
    if x%2==0:
        sum= x + sum
print(sum)



