#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple.
name = "amy"
print(f"Hello, {name.capitalize()}. Are ready for the test?")


#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
name = "amy haddad"

print(name.lower())
print(name.upper())
print(name.title())


#2-5. Famous Quote: Find a quote from a famous person you admire . Print the quote and the name of its author. 
famous_quote = "Continuous effort -- not strength or intellgence -- is the key to unlocking our potential."
quote_author = "winston churchill"

print(f"{quote_author.title()} said,\"{famous_quote}\"")


#2-6. Repeat Exercise 2-5, but this time store the famous per- son’s name in a variable called famous_person. 
# Then compose your message and store it in a new variable called message. Print your message.
famous_person = "winston churchill"
message = (f"{famous_person.capitalize()} said, \"{famous_quote}\"")
print(message)


#2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once
#Print the name once, so the whitespace around the name is displayed.
names = "\tamy haddad\t"
print(names)

# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
names = names.rstrip()
print(names)

names = names.lstrip()
print(names)

names = names.strip()
print(names)
