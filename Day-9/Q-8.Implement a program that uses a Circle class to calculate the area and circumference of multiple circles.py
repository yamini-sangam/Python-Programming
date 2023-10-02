# Implement a program that uses a Circle class to calculate the area and circumference of multiple circles
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

# Example usage
circles = [
    Circle(3),
    Circle(5),
    Circle(7)
]

for index, circle in enumerate(circles, start=1):
    print(f"Circle {index}:")
    print(f"Radius: {circle.radius}")
    print(f"Area: {circle.calculate_area():.2f}")
    print(f"Circumference: {circle.calculate_circumference():.2f}")
    print("-" * 20)
