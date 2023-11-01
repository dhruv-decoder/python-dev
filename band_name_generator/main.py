# Write your code below this line 👇
# print("hello "+input("name:"))
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

#PROJECT-1
import random

#  band name generation.
adjectives = ["Electric", "Sonic", "Mystic", "Cosmic", "Epic", "Funky", "Golden", "Neon", "Wild"]
nouns = ["Dragons", "Explorers", "Harmony", "Revolution", "Rhythm", "Voyage", "Innovators", "Universe", "Legends"]

# Welcome the user to the Band Name Generator.
print("Welcome to the Advanced Band Name Generator!")

# Ask the user for their first name.
first_name = input("What is your first name? ")

# Ask the user for the city they grew up in.
city_name = input("Which city did you grow up in? ")

# Ask the user for the name of their first pet.
pet_name = input("What was the name of your first pet? ")

# Generate a band name by combining user inputs with a random adjective and noun.
random_adjective = random.choice(adjectives)
random_noun = random.choice(nouns)
band_name = f"{random_adjective} {city_name} {random_noun}"

# Display the personalized band name to the user.
print(f"Hello, {first_name}! Your unique band name could be: {band_name}")

