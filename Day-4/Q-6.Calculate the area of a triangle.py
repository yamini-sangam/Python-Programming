# Calculate the area of a triangle given its base and height using a function

def calculate_triangle_area(base, height):
    # Calculate the area using the formula: (1/2) * base * height
    area = (1/2) * base * height
    return area
base = 5.0
height = 8.0
area = calculate_triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is {area}")
