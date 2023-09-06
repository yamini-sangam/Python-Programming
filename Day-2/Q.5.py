# Given a list of names, concatenate them into a single string separated by spaces

names= input("Enter names separated by commas: ")
list= [x for x in names.split(',')]

s=""
for x in list:
    s = s+" "+x
print(s)