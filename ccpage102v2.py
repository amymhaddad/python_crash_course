#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# Print each piece of information stored in your dictionary.
friend = {
    'first_name': 'belina', 
    'last_name': 'smith',
    'city': 'boston',
}

print(friend['first_name'].capitalize())
print(friend['last_name'].capitalize())
print(friend['city'].capitalize())


# Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. 
names_and_fav_numbers = {
    'theo': 10,
    'phil': 9,
    'pam': 8,
    'melinda': 7,
    'sarah': 6,
}

# Option 1: Printing each person's name and number
for name, number in names_and_fav_numbers.items():
    print(f"\nName: {name.capitalize()}")
    print(f"Favorite number: {number}")

# Option 2: printing person's name and number
print(f"Theo's favorite number is: {names_and_fav_numbers['theo']}.")
print(f"Phil's favorite number is: {names_and_fav_numbers['phil']}.")
print(f"Pam's favorite number is: {names_and_fav_numbers['pam']}.")
print(f"Melinda's favorite number is: {names_and_fav_numbers['melinda']}.")
print(f"Sarah's favorite number is: {names_and_fav_numbers['sarah']}.")


# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
glossary = {
    'len': 'get the length of an object',
    'input': 'information from the user',
    'string': 'characters within quotes',
    'object': 'something that can be manipulated',
}

# Option 1: Print each word and its meaning as neatly formatted output.
print(f"len: {glossary['len']}")
print(f"input: {glossary['input']}")
print(f"string: {glossary['string']}")
print(f"object: {glossary['object']}")

print(f"""
len: {glossary['len']}
input: {glossary['input']}
string: {glossary['string']}
object: {glossary['object']}
""")

# Option 2: Print each word and its meaning as neatly formatted output.
for term, definition in glossary.items():
    print(f"\nTerm: {term}")
    print(f"Definition: {definition}")
