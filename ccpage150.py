#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
magicians = ['ed', 'bob', 'sherry']

def show_magicians(names):
    """Tell show magicians"""
    for name in names:
        print(name)
 

show_magicians(magicians[:])


# Write a function called make_great() that modifies the list of magicians by add- ing the phrase the Great to each magician’s name. 
# Call show_magicians() to see that the list has actually been modified.
def make_great(names):
    """Add "the Great" to each magician name"""
    for name in names: 
        magician_name = name + " the Great"
        print(magician_name)

make_great(magicians)

show_magicians(magicians)


# Start with your work from Exercise 8-10 . Call the function make_great() with a copy of the list of magicians’ names.
# Because the original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the origi- nal names and one list with the Great added to each magician’s name.
magicians = ['ed', 'bob', 'sherry']
new_list_magicians = magicians[:]

def make_great(names):
    """List "the great" magicians using a copy of the list"""
    for name in names:
        magician_name = name + " the Great"
        print(magician_name)

make_great(new_list_magicians)
make_great(magicians)
