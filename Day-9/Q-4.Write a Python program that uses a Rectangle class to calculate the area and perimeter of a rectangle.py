# Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Get input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create a rectangle object
rectangle = Rectangle(length, width)

# Calculate area and perimeter
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

# Display the results
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
