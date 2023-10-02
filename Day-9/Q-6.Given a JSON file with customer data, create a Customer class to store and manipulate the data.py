# Given a JSON file with customer data, create a Customer class to store and manipulate the data

import json

# Load customer data from JSON file into a dictionary
with open('Customers.json', 'r') as file:
    customer_data = json.load(file)

# Function to find a customer by ID
def find_customer_by_id(customer_id):
    for customer in customer_data['customers']:
        if customer['id'] == customer_id:
            return customer
    return None

# Example usage
customer_id = 1  # Replace this with the desired customer ID
found_customer = find_customer_by_id(customer_id)

if found_customer:
    print("Customer found:")
    print(f"ID: {found_customer['id']}")
    print(f"Name: {found_customer['name']}")
    print(f"Email: {found_customer['email']}")
    print(f"Phone: {found_customer['phone']}")
else:
    print("Customer not found.")
