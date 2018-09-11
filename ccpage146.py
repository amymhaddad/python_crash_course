#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value that’s returned.
Option 1
def city_country (city, country):
    """List a city and its country"""
    print(f"{city.title()}, {country.title()}")

city_country('dublin', 'ireland')
city_country('boston', 'united states')
city_country('rome', 'italy')

Option 2: 
def city_country(city, country):
    """Locate city and its country"""
    location = city + ', ' + country
    return location.title()

city_country_location = city_country('rome', 'italy')
print(city_country_location)

city_country_location = city_country('boston', 'united states')
print(city_country_location)

city_country_location = city_country('dublin', 'ireland')
print(city_country_location)


# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album information correctly.
def make_album(name, title):
    """Describe one album"""
    album_1 = {'first_name': name, 'album_title': title}

    album_2 = {'first_name': name, 'album_title': title}

    album_3 = {'first_name': name, 'album_title': title}

    return album_1
    return album_2
    return album_3

album_1_info = make_album('tom', 'hello 1')
album_2_info = make_album('jim', 'hello 2')
album_3_info = make_album('kim', 'hello 3')

print(album_1_info)
print(album_2_info)
print(album_3_info)


# Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
# If the calling line includes a value for the num- ber of tracks, add that value to the album’s dictionary.
def make_album(name, title, tracks=''):
    """Describe album"""
    album_1 = {'first_name': name, 'title': title}

    if tracks:
        album_1['total_tracks'] = tracks
    
    return album_1

album_info = make_album('jill', 'hello 5', tracks=5)
print(album_info)


# Start with your program from Exercise 8-7 . Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.

def make_album(name, title):
    """Describe album"""
    album_1 = {'full_name': name, 'album_title': title}

    return album_1

while True:
    print("Enter information when prompted. Type 'q' to quit. ")

    f_name = input("Enter your full name: ")
    if f_name == 'q':
        break

    a_title = input("Enter the album title: ")
    if a_title == 'q':
        break

    album_1_info = make_album(f_name, a_title)
    print(album_1_info)
