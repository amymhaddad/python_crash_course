#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import json

filename = 'fav_number.json'

with open(filename) as file_object:
    fav_number = json.load(file_object)
    print(f"I know your favorite number. It's {fav_number}.")
