#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


# Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary.
# Rewrite the program using the OrderedDict class and make sure the order of the
# output matches the order in which key-value pairs were added to the dictionary.
from collections import OrderedDict

python_glossary = OrderedDict()

python_glossary = {
    'list': 'collection of items',
    'range': 'generates series of numbers',
    'input': 'get information from user',
    'len': 'find out umber of characters in an object',
    'for_loop': 'do a repetitve task',
    'conditional': 'a decision making point',
}

for term, definition in python_glossary.items():
    print(f"Term: {term}")
    print(f"Definition: {definition}")
    print('\n')


# Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.

from random import randint

class Die():
    """An attempt to model a dice with a random number"""
    def __init__(self, roll=0, sides=6):
        """Initialize attribute for number of sides on a dice"""
        self.roll = roll
        self.sides = sides

    
    def roll_die(self):
        """Create a method that prints a random number between 1 and 6; roll it 10 times"""
        self.roll = 0
        while self.roll <= 10:
            self.roll += 1
            random_number = randint(1, self.sides)
            if self.roll <= 10:
                print(f"The random number is {random_number}.")
            else:
                break

dice = Die(6)

print(dice.roll_die())

# Make a 10-sided die and a 20-sided die . Roll each die 10 times.
from random import randint

class Die():

    """An attempt to model a dice"""
    def __init__(self, sides=10):
        """Initialize the attribute"""
        self.sides = sides

    def roll_die(self):
        """Roll the dice 20 times and get a random number"""
        roll = 0
        while roll <= 20:
            roll += 1
            random_number = randint(1, self.sides)

            if roll <= 20:
                print(f"The random number is {random_number}.")
            else:
                break

dice = Die(10)

print(dice.roll_die())


# An alternative approach to check for a 10 or 20-sided dice:
from random import randint

class Die():

    """An attempt to model a dice"""
    def __init__(self, roll=0):
        """Initialize the attribute"""
        self.roll = roll
        self.sides_20 = 20
        self.sides_10 = 10

    def roll_die_10(self):

        """Roll the dice 10 times and get a random number"""
        while self.roll <= 10:
            self.roll += 1
            random_number = randint(1, self.sides_10)

            if self.roll < 10:
                print(f"The random number is {random_number}.")

    def roll_die_20(self):

        """Roll the dice 20 times and get a random number"""

        while self.roll <= 20:
            self.roll += 1
            random_number = randint(1, self.sides_20)

            if self.roll <= 20:
                print(f"The random number is {random_number}.")
            else:
                break

dice_10 = Die()

print(dice_10.roll_die_10())

dice_20 = Die()

print(dice_20.roll_die_20())
