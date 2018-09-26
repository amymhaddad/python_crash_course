#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Make two files, cats.txt and dogs.txt.
# Store at least three names of cats in the first file and three names of dogs in the second file.
# Write a program that tries to read these files and print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
# Move one of the files to a dif- ferent location on your system, and make sure the code in the except block executes properly.

# One way to solve this exercise:
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f_object:
            contents = f_object.read()
            print(f"The names from {filename} are:")
            print(contents.title())
            print("\n")
    except FileNotFoundError:
        print(f"The file {filename} is not found.")

# Second way to solve this exercise:
def animal_names(filename):

    """Print the names of the cats and dogs listed in separate files"""
    try: 
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        print(f"The file {filename} is not found.")
    else:
        print(f"The names in {filename} are: \n{contents.title()}\n")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    animal_names(filename)

# Modify your except block in Exercise 10-8 to fail silently if either file is missing.
def animal_names(filename):

    """Print the names of the cats and dogs listed in separate files"""
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError: 
        pass
    else:
        print(f"The names in {filename} are: \n{contents.title()}\n")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    animal_names(filename)

