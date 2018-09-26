#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# 10-6 Write a program that prompts for two numbers . Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.
print("Enter numbers when prompted, and I'll add them together. ")

first_number = input("Enter first number: ")
second_number = input("Enter a second number: ")

try:
    int(first_number)
    int(second_number)
except ValueError:
    print("You must enter two numbers.")
else:
    sum = int(first_number) + int(second_number)
    print(sum)


# 10-7 Wrap your code from Exercise 10-6 in a while loop so the user can
# continue entering numbers even if they make a mistake and enter text instead of a number.
print("Enter two numbers when prompted and I'll add them together.")
print("Type 'q' to quit. ")

while True:
    first_number = input("Enter first number: ")
    if first_number == 'q':
        break

    second_number = input("Enter a second number: ")
    if second_number == 'q':
        break
    try:
        int(first_number)
        int(second_number)
    except ValueError:
        print("You must enter numbers.")
    else:
        sum = int(first_number) + int(second_number)
        print(f"The sum is {sum}.")
