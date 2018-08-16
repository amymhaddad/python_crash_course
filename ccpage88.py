#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


# Write an if-elif-else chain that determines a person's stage of life

import sys

age = int(input("What's your age? "))

# Step 1: write conditional
if age <= 0:
    print("Please enter a valid age.")
    sys.exit()

if age < 2:
    print("You're a baby")
elif age >= 2 and age < 4:
    print("You're a toddler.")
elif age >= 13 and age < 20:
    print("You're a teenager.")
elif age >= 20 and age < 65:
    print("You're an adult.")
else:
    print("You're a senior.")


# Make a list of fruite and write five if statements. 
# Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement.

fruits = ['apples', 'kiwi', 'oranges', 'pinapple', 'cherries']

if "apples" in fruits:
    print("Apple season is coming soon!")

if "bananas" not in fruits:
    print("Each week I forget to buy bananas!")

if "mangos" not in fruits:
    fruits.append("mango")
    print("I also enjoy eating mangos!")

if "mango" in fruits:
    print("A mango smoothie is my favorite.")

if "kiwi" in fruits:
    fruits.remove("kiwi")
    print("Kiwis aren't one of my favorite fruits.")
