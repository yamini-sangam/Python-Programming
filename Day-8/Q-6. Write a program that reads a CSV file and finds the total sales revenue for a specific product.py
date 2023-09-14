#  Write a program that reads a CSV file and finds the total sales revenue for a specific product

import csv

# Function to find the total sales revenue for a specific product in a CSV file
def total_sales_revenue_for_product(csv_filename, product_name):
    try:
        total_revenue = 0

        with open(csv_filename, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                product = row['Product']
                revenue = int(row['Revenue'])

                if product == product_name:
                    total_revenue += revenue

        return total_revenue
    except FileNotFoundError:
        print(f"File not found: {csv_filename}")
        return None

# Specify the CSV file path and the product name you want to find the revenue for
csv_filename = 'sales_data.csv'  # Replace with the path to your CSV file
product_name = 'ProductA'  # Replace with the product name you want to find

# Find the total sales revenue for the specified product
revenue_for_product = total_sales_revenue_for_product(csv_filename, product_name)

if revenue_for_product is not None:
    print(f"Total sales revenue for {product_name}: ${revenue_for_product}")
