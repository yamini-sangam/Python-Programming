# Given a CSV file with product details (name, price, quantity), create a Product class to manage the data

import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)  # Assuming price is a numeric value
        self.quantity = int(quantity)  # Assuming quantity is an integer

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print("-" * 20)

# Function to load product data from CSV file
def load_products_from_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            name, price, quantity = row
            product = Product(name, price, quantity)
            products.append(product)
    return products

# Example usage
products = load_products_from_csv('products.csv')

# Display product information
for product in products:
    product.display_info()
