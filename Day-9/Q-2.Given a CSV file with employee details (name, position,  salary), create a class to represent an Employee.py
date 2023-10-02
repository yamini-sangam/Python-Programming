# Given a CSV file with employee details (name, position, salary), create a class to represent an Employee

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary:.2f}"

# Example usage:
# Assuming you have read employee details from a CSV file and created instances of the Employee class
employee1 = Employee("John Doe", "Manager", 60000.00)
employee2 = Employee("Jane Smith", "Developer", 50000.00)

# Printing employee details
print(employee1)
print(employee2)
