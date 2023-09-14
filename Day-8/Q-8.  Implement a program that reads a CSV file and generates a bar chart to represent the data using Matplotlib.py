#  Implement a program that reads a CSV file and generates a bar chart to represent the data using Matplotlib

import csv
import matplotlib.pyplot as plt

# Function to read CSV data and generate a bar chart
def generate_bar_chart(csv_filename):
    categories = []
    values = []

    try:
        with open(csv_filename, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                categories.append(row['Category'])
                values.append(int(row['Value']))

        # Create the bar chart
        plt.figure(figsize=(8, 6))  # Set the figure size (optional)

        plt.bar(categories, values)
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title('Bar Chart of Data')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        plt.tight_layout()  # Adjust layout
        plt.show()
    except FileNotFoundError:
        print(f"File not found: {csv_filename}")

# Specify the CSV file path
csv_filename = 'data.csv'  # Replace with the path to your CSV file

# Call the generate_bar_chart function
generate_bar_chart(csv_filename)
