#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#Use a for loop to print the numbers 1 to 20, inclusive
for value in range(1,20):
    print(value)


#Make a list of numbers from 1 to one million and then use a for loop to print the numbers
numbers = list(range(1, 1000000))
print(numbers)

numbers = []
for value in range(1, 1000000):
    numbers.append(value)
print(numbers)


#Make a list of numbers from one to one million, then use min(), max(), and sum()
numbers = [1, 1000000]
print(min(numbers))
print(max(numbers))
print(sum(numbers))


#Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

for value in range(1,20,2):
    print(value)

new_list = list(range(1,20,2))
print(new_list) 

#alternative:
numbers = list(range(1,20,2))
print(numbers)

#alternative:
numbers = []
for value in range(1,20,2):
    numbers.append(value)
print(numbers)


#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
for value in range(3,30,3):
    print(value)

new_list = list(range(3,30,3))
print(new_list)

#alternative:
second_list = []
for value in range(3,30,3):
    second_list.append(value)
print(second_list)


#Make a list of the first 10 cubes (ie, the cube of each integer from 1-10), and use a for loop to print the value of each cube
cubes = []
for value in range(1,10):
    cube = value**3
    cubes.append(cube)
print(cubes)


#Use a list comprehension to generate a list of the first 10 cubes:
cubes = [value**3 for value in range(1,10)]
print(cubes)
