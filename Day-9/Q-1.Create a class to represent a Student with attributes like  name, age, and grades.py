# Create a class to represent a Student with attributes like name, age, and grades

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {', '.join(map(str, self.grades))}"

# Example usage:
student1 = Student("John Doe", 18, [90, 85, 88])
print(student1)
print(f"Average Grade: {student1.get_average_grade()}")
