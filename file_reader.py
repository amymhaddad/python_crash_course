#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Print the content of "contents" 3 times:
for content in range(3):
    print(contents)


# Print content by reading the entire file:
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)


# Print content by looping over the file object with open('learning_python.txt') as file_object:
file_name = 'learning_python.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())


# Print content by storing lines in a list and work with them outside the with block
# with open('learning_python.txt') as file_object:
with open('learning_python.txt') as file_object:
    contents = file_object.readlines()

content_string = ' '
for content in contents:
    content_string += content

print(content_string)


# Read in each line from the file you just created, learning_python.txt,
# and replace the word Python with the name of another language, such as C . Print each modified line to the screen.
with open('learning_python.txt') as file_object:
    contents = file_object.readlines()

for content in contents:
    if "Python" in content:
        update_language = content.replace("Python", "C")
        print(update_language.strip())
              