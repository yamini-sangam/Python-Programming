# Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees

import csv

# Function to calculate the average salary of employees from a CSV file
def calculate_average_salary(csv_filename):
    try:
        total_salary = 0
        num_employees = 0

        with open(csv_filename, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                salary = float(row['Salary'])
                total_salary += salary
                num_employees += 1

        if num_employees == 0:
            return 0  # Avoid division by zero if there are no employees

        average_salary = total_salary / num_employees
        return average_salary
    except FileNotFoundError:
        print(f"File not found: {csv_filename}")
        return None

# Specify the CSV file path
csv_filename = 'employee_details.csv'  # Replace with the path to your CSV file

# Calculate the average salary
average_salary = calculate_average_salary(csv_filename)

if average_salary is not None:
    print(f"Average salary of all employees: ${average_salary:.2f}")
