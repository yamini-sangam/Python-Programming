# Calculate the area and circumference of a circle given its radius

import math

# Input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius**2

# Calculate the circumference of the circle
circumference = 2 * math.pi * radius

# Display the results
print(f"The area of the circle with radius {radius} is {area:.2f}")
print(f"The circumference of the circle with radius {radius} is {circumference:.2f}")

