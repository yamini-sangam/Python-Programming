# Given a CSV file with student names and scores, find the student with the highest score

import csv


# Function to find the student with the highest score in a CSV file
def find_student_with_highest_score(csv_filename):
    highest_score = float("-inf")  # Initialize with negative infinity to ensure any score is higher
    student_with_highest_score = None

    with open(csv_filename, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            name = row['Name']
            score = int(row['Score'])

            if score > highest_score:
                highest_score = score
                student_with_highest_score = name

    return student_with_highest_score, highest_score


# Specify the CSV file path
csv_filename = 'student_scores.csv'  # Replace with the path to your CSV file

# Find the student with the highest score
student, highest_score = find_student_with_highest_score(csv_filename)

# Print the result
print(f"The student with the highest score is {student} with a score of {highest_score}.")
