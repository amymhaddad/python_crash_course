#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Make a class called Restaurant.
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indi- cating that the restaurant is open.
# Make an instance called restaurant from your class . Print the two attri- butes individually, and then call both methods.

class Restaurant():
    """An attempt to model a restaurant"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name.title()} is the name of the restaurant.")
        print(f"{self.name.title()} serves {self.cuisine.title()} food.")

    def open(self):
        """Indicate whether the restaurant is open"""
        print(f"{self.name.title()} is open today.")
    
restaurant = Restaurant('grotto', 'italian')
print(f"My favorite restaurant is called {restaurant.name.title()}.")
print(f"{restaurant.name.title()} serves {restaurant.cuisine.title()} food.")

restaurant.describe_restaurant()
restaurant.open()


# Start with your class from Exercise 9-1 (exercise listed above).
# Create three different instances from the class, and call describe_restaurant() for each instance.
class Restaurant():
    """An attempt to model a restaurant"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """Write two sentences that describe a restaurant"""
        print(f"The name of the restaurant is: {self.name.title()}.")
        print(f"{self.name.title()} serves {self.cuisine.title()} food.")

    def open(self):
        """Indicate if restaurant is open"""
        print(f"{self.name.title()} is open today.")

my_fav_restaurant = Restaurant('aqua al 2', 'italian')
my_fav_restaurant.describe_restaurant()

your_fav_restaurant = Restaurant('posto', 'italian')
your_fav_restaurant.describe_restaurant()

steakhouse_restaurant = Restaurant('j gilberts', 'american')
steakhouse_restaurant.describe_restaurant()


# Make a class called User.
# Create two attributes called first_name and last_name, and then create several
# other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
class User():
    """An attempt to model a user"""
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
    
    def describe_user(self):
        """Summarize information about the user"""
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"{self.first_name.title()} lives in {self.location.title()} and is {self.age} years old.")
    
    def greet_user(self):
        """Write a personalized greeting to user"""
        print(f"Hello, {self.first_name.title()}!")

user_1 = User('shara', 'bradley', 'maine', 30)
user_1.describe_user()
user_1.greet_user()

user_2 = User('tom', 'smith', 'florida', 60)
user_2.describe_user()
user_2.greet_user()

user_3 = User('mack', 'mcdonald', 'texas', 15)
user_3.describe_user()
user_3.greet_user()
