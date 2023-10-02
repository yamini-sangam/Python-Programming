# Create a class to represent a Car with attributes like make, model, and year

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

# Example usage of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2021)

car1.display_info()  # Output: Car Info: 2022 Toyota Camry
car2.display_info()  # Output: Car Info: 2021 Ford Mustang
