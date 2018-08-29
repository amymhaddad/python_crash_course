#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Make a list called sandwich_orders and fill it with the names of vari- ous sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

# Step 1: create two lists to move items from one to another
finished_sandwiches = []
sandwich_orders = ['tuna', 'beef', 'peanut butter', 'ham']

# use while loop to loop through the orders in sandwich_orders
while sandwich_orders:
    completed_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(completed_sandwich)
    
print("These are the finished sandwiches: ")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.capitalize()}")


# Make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

# Step 1: create list with "pastrami" appearing three times
sandwich_orders = ['tuna', 'pastrami', 'beef', 'pastrami', 'pastrami', 'peanut butter', 'ham']
finished_sandwiches = []

# Step 2: remove all instances of pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    completed_sandwhiches = sandwich_orders.pop()
    finished_sandwiches.append(completed_sandwhiches)

print("These are the finished sandwiches: ")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.capitalize()}")


# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

# Create empty dictionary to add responses to
responses = {}

# Write while loop to gather responses
active = True
while active:
    name = input("What's your name? ")
    dream_vacation_location = input("Where do you want to travel to? ")

    responses[name] = dream_vacation_location

    print("Is there another person who should take this poll?")
    repeat_with_new_user_input = input("Type: 'yes' or 'no': ")
    normalized_repeat_with_new_user_input = repeat_with_new_user_input.lower()

    if normalized_repeat_with_new_user_input == 'no':
        active = False
    
# Write loop to print results
print("These are the results of the poll: ")
for name, location in responses.items():
    print(f"Name: {name.capitalize()}")
    print(f"Dream Vacation Location: {location.capitalize()}")
    print('\n')
