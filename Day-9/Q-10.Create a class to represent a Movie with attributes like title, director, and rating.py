# Create a class to represent a Movie with attributes like title, director, and rating

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Rating: {self.rating}")
        print("-" * 20)

# Example usage
movie1 = Movie("Inception", "Christopher Nolan", "PG-13")
movie2 = Movie("The Dark Knight", "Christopher Nolan", "PG-13")
movie3 = Movie("Pulp Fiction", "Quentin Tarantino", "R")

# Display movie information
print("Movie 1:")
movie1.display_info()
print("Movie 2:")
movie2.display_info()
print("Movie 3:")
movie3.display_info()
