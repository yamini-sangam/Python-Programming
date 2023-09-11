#  Create a function to find the square of each element in a given list

def square_elements(input_list):
    # Use a list comprehension to find the square of each element
    squared_list = [x ** 2 for x in input_list]
    return squared_list

my_list = [1,2,3,4,5]
result = square_elements(my_list)
print(result)





