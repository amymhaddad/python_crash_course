#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


# Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people . As you loop through the list, print everything you know about each person.
friend_1 = {
    'first_name': 'belina',
    'last_name': 'smith',
    'city': 'boston',
}

friend_2 = {
    'first_name': 'bob',
    'last_name': 'mangia',
    'city': 'columbus',
}
    
friend_3 = {
    'first_name': 'sam',
    'last_name': 'smith',
    'city': 'austin',
}

people = [friend_1, friend_2, friend_3]

for friend in people: 
    full_name = friend['first_name'].capitalize() + ' ' + friend['last_name'].capitalize()
    friend_city = friend['city'].capitalize()
    print(f"\n{full_name} lives in {friend_city}.")


# Make several dictionaries, where the name of each dictionary is the name of a pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets.
# Next, loop through your list and as you do print everything you know about each pet.
pets = {
    'toby': {
        'animal_type': 'dog',
        'owner_name': 'posie',
        },
    'elle': {
        'animal_type': 'cat',
        'owner_name': 'david',
        },
    'kitty': {
        'animal_type': 'hampster',
        'owner_name': 'chris',
        },
}

for pet_name, pet_info in pets.items():
    print(f"Pet name: {pet_name.capitalize()}")
    print(f"Animal type: {pet_info['animal_type'].capitalize()}")
    print(f"Owner name: {pet_info['owner_name'].capitalize()}")
    print('\n')

# Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
# Loop through the dictionary, and print each person’s name and their favorite places.
favorite_places = {
    'sal': ['canada', 'ireland'],
    'missy': ['new mexico', 'england', 'montana'],
    'sam': ['ohio', 'new york', 'los angeles'],
}

for name, places in favorite_places.items():
    print(f"\nThese are {name.capitalize()}'s favorite places:")
    for place in places:
        print(place.title())


# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers .
names_and_fav_numbers = {
    'theo': [101, 200],
    'phil': [12, 00],
    'pam': [50, 5, 10],
    'melinda': [1, 21],
    'sarah': [12, 10]
}

for name, numbers in names_and_fav_numbers.items():
    print(f"\nThese are {name.capitalize()}'s favorite numbers: ")
    for number in numbers:
        print(number)


# Make a dictionary called cities.
# Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city.
# The keys for each city’s dictionary should be something like country, population, and fact
# Print the name of each city and all of the infor- mation you have stored about it.
cities = {
    'boston': {
        'country': 'usa',
        'approximate_population': '600,000',
        'famous_food': 'lobster',
    },
    'dublin': {
        'country': 'ireland',
        'approximate_population': '500,000',
        'famous_food': 'soda bread',
    },
    'columbus': {
        'country': 'usa',
        'approximate_population': '800,000', 
        'famous_food': 'buckeyes',
    },
}

for city, city_info in cities.items():
    if city_info['country'] == 'usa':
        city_info['country'] = 'USA'
    else:
        city_info['country'] = city_info['country'].capitalize()

    print(f"""
    \nCity: {city.capitalize()}
    \tCountry: {city_info['country']}
    \tApproximate Population: {city_info['approximate_population']}
    \tFamous food: {city_info['famous_food']}
    """)


# Use one of the example pro- grams from this chapter, and extend it by adding new keys and values,
# changing the context of the program or improving the formatting of the output.
pizza_types = {
    'crusts': ['thin', 'thick', 'deep dish'],
    'toppings': ['pepporoni', 'mushroom', 'cheese'],
    'sauces': ['spicy', 'mild', 'alfredo'],
}

for category, options in pizza_types.items():
    print(f"Category: {category.capitalize()}")
    for option in options:
        print(f"{option.capitalize()}")
    print("\n")
