#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text .

def read_text(filename):
    """Read a text and count the number of instances a word appears"""
    try: 
        with open(filename) as f_object:
            contents = f_object.read()
    except ValueError:
        print(f"The file {filename} is not found.")
    else: 
        normalized_contents = contents.lower()
        line_count = normalized_contents.count("the")
        print(f"The file {filename} contains {line_count} instances of the word \'the.\'")

read_text('son_of_tarzan.txt')
