#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Write a program that prompts the user for their name. 
# When they respond, write their name to a file called guest.txt.
filename = 'ccpage199_guests.txt'

name = input("Enter your name: ")

with open(filename, 'w') as file_object:
    file_object.write(name.title())


# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and
# add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.
message = "Enter your name when prompted. "
message += "Type 'q' to quit. "

filename = 'ccpage199_guest_book.txt'

while True: 
    name = input(message)

    if name == 'q':
        break
    else: 
        with open(filename, 'a') as file_object:
            file_object.write(f"Name: {name.title()}\n")
            file_object.write(f"Welcome, {name.title()}!\n")
            file_object.write("Your stay begins today, on September 25, 2018.\n")
            file_object.write("\n")
  