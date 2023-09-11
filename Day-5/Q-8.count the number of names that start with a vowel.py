# Given a list of names, count the number of names that start with a vowel

def count_names_starting_with_vowel(name_list):
    # Define a set of lowercase vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Initialize a variable to keep track of the count
    count = 0

    # Iterate through the names in the list
    for name in name_list:
        # Convert the first character of the name to lowercase and check if it's in the set of vowels
        if name[0].lower() in vowels:
            count += 1

    return count
name_list = ["Alice", "Bob", "Eve", "Irene", "Oliver", "Ursula"]
count = count_names_starting_with_vowel(name_list)
print(f"Number of names starting with a vowel: {count}")
