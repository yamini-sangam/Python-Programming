# Write a program that finds the largest and smallest elements in a list
def find_smallest_largest(lst):
    if len(lst) == 0:
        return None, None  # Return None for both smallest and largest if the list is empty

    smallest = largest = lst[0]  # Initialize the variables with the first element of the list

    for num in lst:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
smallest, largest = find_smallest_largest(my_list)

if smallest is not None and largest is not None:
    print(f"The smallest element is: {smallest}")
    print(f"The largest element is: {largest}")
else:
    print("The list is empty.")
