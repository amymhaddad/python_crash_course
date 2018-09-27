#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import json

filename = 'fav_number.json1'
try:
    with open(filename) as file_object:
        fav_number = json.load(file_object)
except FileNotFoundError:
    fav_number = input("Enter your favorite number: ")
    with open(filename, 'w') as file_object:
        json.dump(fav_number, file_object)
        print(f"Your favorite number is {fav_number}.")
else: 
    print(f"I remember your favorite number! It's {fav_number}.")
