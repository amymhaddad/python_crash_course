#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import json

filename = 'fav_number.json'

fav_number = input("Enter your favorite number: ")

with open(filename, 'w') as file_object:
    json.dump(fav_number, file_object)
    