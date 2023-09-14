# Write a function that reads a JSON file and extracts specific information from it

import json

# Function to read a JSON file and extract specific information
def extract_information_from_json(json_filename):
    try:
        with open(json_filename, 'r') as file:
            data = json.load(file)
            name = data.get('name', 'N/A')
            age = data.get('age', 'N/A')
            email = data.get('email', 'N/A')

            address = data.get('address', {})
            street = address.get('street', 'N/A')
            city = address.get('city', 'N/A')
            state = address.get('state', 'N/A')

            return {
                'Name': name,
                'Age': age,
                'Email': email,
                'Street': street,
                'City': city,
                'State': state
            }
    except FileNotFoundError:
        print(f"File not found: {json_filename}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_filename}")
        return None

# Specify the JSON file path
json_filename = 'data.json'  # Replace with the path to your JSON file

# Call the extract_information_from_json function
result = extract_information_from_json(json_filename)

if result is not None:
    for key, value in result.items():
        print(f"{key}: {value}")
