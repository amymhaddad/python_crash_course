#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sand- wich that is being ordered.
# Call the function three times, using a different num- ber of arguments each time.

def make_sandwich(*sandwich_items):
    """List items on a sandwich"""
    print(sandwich_items)


make_sandwich('lettuce', 'peppers', 'onions')

make_sandwich('cheese', 'ham')

make_sandwich('bread', 'jelly')


# Alternative
def make_sandwich(*sandwich_items):
    """Make a sandwich with an unlimited number of items"""
    print("These are the items on your sandwich: ")
    for item in sandwich_items:
        print(f"- {item}")

make_sandwich('cheese', 'ham', 'mayo')

# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary about myself"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, values in user_info.items():
        profile[key] = values


    return profile


profile_info = build_profile('amy', 'haddad', age=34, location='boston')
print(profile_info)


# Alternative:
def build_profile(first, last, age, location, food):
    """Build a profile that describes me"""
    my_profile = {
        'first_name': first,
        'last_name': last, 
        'current_age': age,
        'current_location': location, 
        'favorite_food': food,
    }
    return my_profile


amy_info = build_profile(first='amy',
                        last='haddad',
                        age=34,
                        location='boston',
                        food='baklava')

print(amy_info)


# Write a function that stores information about a car in a diction- ary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the func- tion with the required information and two other name-value pairs

def car(manufacturer, model, **car_info):
    """Info about a car"""
    new_car = {}
    new_car['manu_name'] = manufacturer
    new_car['model_name'] = model
    for key, values in car_info.items():
        new_car[key] = values

    return new_car


toyota_info = car('toyota', 't_1', year=2018, miles=1000)
print(toyota_info)


# Alternative:
def car(manufacturer, model, **car_info):
    """Create a dictionary about a car"""
    car_stats = {'car_manufacturer': manufacturer, 'car_model': model}
    for key, values in car_info.items():
        car_stats[key] = values
    return car_stats

toyota = car('toyota', 
            't-10', 
            year=2012, 
            miles=100000)
print(toyota)

