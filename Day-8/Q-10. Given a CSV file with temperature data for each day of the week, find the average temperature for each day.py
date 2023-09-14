#  Given a CSV file with temperature data for each day of the week, find the average temperature for each day

import csv
from collections import defaultdict

# Function to calculate the average temperature for each day of the week
def calculate_average_temperature(csv_filename):
    try:
        # Use defaultdict to store temperatures for each day
        day_temperatures = defaultdict(list)

        with open(csv_filename, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                day = row['Day']
                temperature = float(row['Temperature'])
                day_temperatures[day].append(temperature)

        # Calculate average temperature for each day
        average_temperatures = {}
        for day, temperatures in day_temperatures.items():
            average_temp = sum(temperatures) / len(temperatures)
            average_temperatures[day] = average_temp

        return average_temperatures
    except FileNotFoundError:
        print(f"File not found: {csv_filename}")
        return None

# Specify the CSV file path
csv_filename = 'temperature_data.csv'  # Replace with the path to your CSV file

# Call the calculate_average_temperature function
average_temperatures = calculate_average_temperature(csv_filename)

if average_temperatures is not None:
    for day, average_temp in average_temperatures.items():
        print(f"Average temperature for {day}: {average_temp:.2f}°C")
