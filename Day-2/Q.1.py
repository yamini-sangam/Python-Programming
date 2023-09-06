# Given a list of numbers, find the sum and average

numbers= input("Enter numbers separated by commas: ")
list= [int(x) for x in numbers.split(',')]

len= len(list)
if len >0:
    print("sum: ",sum(list))
    print("avg: ", sum(list)//len)