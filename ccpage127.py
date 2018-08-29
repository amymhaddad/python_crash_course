#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
prompt = "Enter a pizza topping. "
prompt += "(Type 'quit' when finished) "

toppings = ""
while toppings != 'quit':
    toppings = input(prompt)

    if toppings != 'quit':
        print(f"Adding {toppings} to your pizza!")


# A movie theater charges different ticket prices depending on a person’s age . If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
age = "Tell me your age and I'll tell you the price of admission."
age += "\nType 'quit' when finished. "

active = True
while active:
    guest_age = input(age)

    if guest_age == 'quit':
        active = False
    else:
        guest_age = int(guest_age)
        if guest_age < 0:
            print("Please enter a valid age.")
        elif guest_age >= 0 and guest_age < 3:
            print("You're free!")
        elif guest_age >= 3 and guest_age <= 12:
            print("You're cost is $10.")
        else:
            print("Your cost is $15.")


# Write different versions of either Exercise 7-4 and do each of the following once:
# Use a conditional test in the while statement to stop the loop:
toppings = 1
while toppings <= 5:
    toppings += 1
    print(toppings)

# Use an active variable to control how long the loop runs
prompt = "Enter the pizza ingredients when prompted. "
prompt += "Type 'quit' when finished."
print(prompt)

print("\n")

active = True
while active:
    topping = input("Enter a topping you want to add to your pizza: ")

    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")

# Use a break statement
pizza_info = "Enter a pizza topping: "
pizza_info += "(Type 'done' when your done adding your toppings.) "

while True:
    topping = input(pizza_info)

    if topping == 'done':
        break
    else:
        print(f"Adding {topping} to your pizza.")
