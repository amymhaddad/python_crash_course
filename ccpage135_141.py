#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter.
def display_message():
    """Share what I'm learning about in this chapter"""
    print("I'm learning about functions.")

display_message()


# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message.
def favorite_book(title):
    """Tell my favorite book"""
    print(f"My favorite book is {title.title()}.")

favorite_book('curious george')


# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt(size, text):
    """Describe t-shirt"""
    print(f"The t-shirt is size {size} and says \'{text}.\'")

make_shirt('small', 'i love python')
make_shirt(text = 'hello world', size = 'medium')


# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(text = 'i love python', size = 'large'):
    """Describe shirt"""
    print(f"The shirt is size {size} and says \'{text}.\'")

large_shirt = make_shirt()
meduim_shirt = make_shirt(size = 'medium')
small_shirt = make_shirt(size = 'small', text = 'boston')


# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland.
# Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country = 'united states'):
    """Describe a city"""
    print(f"{city.title()} is in the {country.title()}.")
    print(f"{city.title()} is the capital.")
    print(f"{city.title()} has good food.")

describe_city(city = 'boston')
describe_city(city = 'providence')
describe_city(city = 'dublin', country = 'ireland')
