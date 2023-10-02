# Write a program that uses a Person class to keep track of a person's name, age, and address

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

# Example usage
person1 = Person("Alice", 30, "123 Main St, Cityville")
person2 = Person("Bob", 25, "456 Elm St, Townsville")

print("Person 1:")
person1.display_info()
print("\nPerson 2:")
person2.display_info()

