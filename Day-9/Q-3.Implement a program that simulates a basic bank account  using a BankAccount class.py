# Implement a program that simulates a basic bank account using a BankAccount class

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Rating: {self.rating}"

# Example usage:
movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 9.3)
movie2 = Movie("The Godfather", "Francis Ford Coppola", 9.2)

print(movie1)
print(movie2)
