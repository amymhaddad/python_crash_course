#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.

class Restaurant():
    """An attempt to model a restaurant"""

    def __init__(self, restaurant_name, restaurant_cuisine, number_served=0):
        """Initialize the attributes"""
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine
        self.number_served = number_served

    def describe_restaruant(self):
        """Write a variable that returns a summary of the restaurant"""
        restaurant_details = self.restaurant_name.title() + " serves " + self.restaurant_cuisine.title() + " food."
        return restaurant_details

    # Add a method so I can set the number of guests served
    def set_number_served(self, guests):
        """Determine the number of people served at the restaurant"""
        self.number_served = guests

    # Add a method to increment the total number of people served
    def increment_number_served(self, incremented_guests):
        """Increment the total number of guests served"""
        self.number_served += incremented_guests

    # I added a method here so I can call the method, instead of printing a statment about the total number of guests served
    def statement_for_number_served(self):
        """Print a statement that tells the number of people served"""
        print(f"The total number of people served is {self.number_served}.")

restaurant = Restaurant('grotto', 'italian')
print(restaurant.describe_restaruant())
print(f"{restaurant.restaurant_name.title()} has served {restaurant.number_served} people.")

print('\n')

restaurant.number_served = 120
restaurant.statement_for_number_served()

print('\n')

restaurant.set_number_served(200)
restaurant.statement_for_number_served()

print('\n')

restaurant.increment_number_served(25)
restaurant.statement_for_number_served()

print('\n')

restaurant.increment_number_served(25)
restaurant.statement_for_number_served()


# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).
# Write a method called increment_ login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_ attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().

class User():
    """An attempt to model a user"""
    def __init__(self, first, last):
        """Initialize the attributes"""
        self.first = first
        self.last = last
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        """Increment the login attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0
    
    def print_login_attempts(self):
        """Pring the user's login attempts"""
        if self.login_attempts == 0:
            print("Your login attempts has been reset to 0.")
        elif self.login_attempts >= 1:
            print(f"You've attempted to login {self.login_attempts} times.")
        else:
            print(f"You've attempted to login {self.login_attempts} time.")

user = User('amy', 'haddad')
user.increment_login_attempts()
user.increment_login_attempts()
user.print_login_attempts()

user.reset_login_attempts()
user.print_login_attempts()
