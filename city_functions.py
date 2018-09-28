#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# 11-1
# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such as Santiago, Chile.
# Store the function in a module called city _functions.py.
def city_country(city, country):
    """Create a city, country combination"""

    city_country_combination = city.title() + ', ' + country.title()
    return city_country_combination


# 11-2
# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such as Santiago, Chile.
# Store the function in a module called city _functions.py.

def city_country(city, country, population=''):
    """Get information about a city"""

    if population:
        city_info = city.title() + ', ' + country.title() + ' - ' + str(population)
    else:
        city_info = city.title() + ', ' + country.title()
    return city_info
