#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def make_shirt(size, text):
    """Describe t-shirt"""
    print(f"The t-shirt is size {size} and says \'{text}.\'")

make_shirt('small', 'i love python')

make_shirt(text='hello world', size='medium')


def describe_city(city, country='united states'):
    """Describe a city"""
    print(f"{city.title()} is in the {country.title()}.")
    print(f"{city.title()} is the capital.")
    print(f"{city.title()} has good food.")

describe_city(city='boston')