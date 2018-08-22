#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Create a glossary of terms in Python.
# Use a loop to run through the dictionary's keys and values.
python_glossary = {
    'list': 'collection of items',
    'range': 'generates series of numbers',
    'input': 'get information from user',
    'len': 'find out umber of characters in an object',
    'for_loop': 'do a repetitve task',
    'conditional': 'a decision making point',
}

for term, definition in python_glossary.items():
    print(f"\nTerm: {term}")
    print(f"Definition: {definition}")


# Make a dictionary containing three major rivers and the country each river runs through.
# Then use a loop to print a sentence about each river.
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states', 
    'missouri': 'united states'
}

us_rivers = ['missouri', 'mississippi']

for river in rivers.keys():
    if river in us_rivers:
        print(f"The {river.capitalize()} River is in the United States.")
    else:
        print(f"The {river.capitalize()} River is in Egypt.")
    
# An alternative way to say something about each river without a list:
for river, country in rivers.items():
    if country == 'usa':
        print(f"{river.capitalize()} River is in the {country.upper()}.")
    else:
        print(f"{river.capitalize()} River is in {country.capitalize()}.")
        

# Use a loop to print the name of each river included in the dictionary.
for name in rivers.keys():
    print(f"{name.capitalize()} River")


# Use a loop to print the name of each country included in the dictionary.
for country in rivers.values():
    print(f"{country.title()}")


# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
people_to_take_poll = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'sam': 'python',
    'ty': 'javascript',
    'pam': 'c',
}

people_who_completed_poll = ['jen', 'ty', 'phil', 'paul', 'amy', 'chris', 'george']

# Loop through the list of people who should take the poll.
for person in people_to_take_poll.keys():
    if person in people_who_completed_poll:
        print(f"Thank you, {person.capitalize()}, for taking the poll!")
    else:
        print(f"{person.capitalize()}, please take the poll!")
        
