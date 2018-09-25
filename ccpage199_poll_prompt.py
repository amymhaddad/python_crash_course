#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""
# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file that stores all the responses.
filename = 'ccpage199_poll_results.txt'

print("Enter you information when prompted.")
print("Type 'q' to quit. ")

while True: 
    user_name = input("Enter your name: ")

    if user_name == 'q':
        break
    else:
        user_reason = input("Enter your reason: ")
        with open(filename, 'a') as file_object:
            file_object.write(f"Name: {user_name.title()}\n")
            file_object.write(f"Reason: {user_reason}\n")
            file_object.write("\n")
            