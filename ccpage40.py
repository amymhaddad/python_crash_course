#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.
names = ['fred', 'tom', 'sam']
print(names[0].capitalize())
print(names[1].capitalize())
print(names[-1].capitalize())

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
print(f"Welcome to Texas, {names[0].capitalize()}!")
print(f"{names[1].capitalize()}, here's the list of ingredients:\nmilk,\nbread, and\ncheese.")
print(f"{names[-1].capitalize()}, let's go to the game today.")


#3-3. Your Own List: Think of your favorite mode of transportation
#and make a list that stores several examples . Use your list to print a series of statements about these items.
transportation = ['walk', 'train', 'car', 'uber']

fav_transport = transportation[0]+"ing"

print(f"{fav_transport.capitalize()} is my preferred mode of transportation.")
print(f"I often take an {transportation[-1].capitalize()} ride to far away places.")
print(f"The {transportation[1]} is a fast way to travel.")
print(f"I don't like to travel by {transportation[2]}.")