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


# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary about myself"""
    profile_1 = {}
    profile_1['first_name'] = first
    profile_1['last_name'] = last
    for key, values in user_info.items():
        profile_1[key] = values


    return profile_1


profile_info = build_profile('amy', 'haddad', age=34, location='boston')
print(profile_info)


# Write a function that stores information about a car in a diction- ary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the func- tion with the required information and two other name-value pairs

def car(manufacturer, model, **car_info):
    """Info about a car"""
    toyota = {}
    toyota['manu_name'] = manufacturer
    toyota['model_name'] = model
    for key, values in car_info.items():
        toyota[key] = values

    return toyota


toyota_info = car('toyota', 't_1', year=2012, miles=1000)
print(toyota_info)
