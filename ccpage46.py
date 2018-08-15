#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
guests = ['mike', 'tom', 'henry']

print(f"{guests[0].capitalize()}, you're invited to dinner.")
print(f"{guests[1].capitalize()}, you're invited to dinner.")
print(f"{guests[-1].capitalize()}, you're invited to dinner.")


# Add a print statement stating the name of the guest who can’t make it. Replace this person with someone else.
print(f"{guests[0].capitalize()} can't make it to dinner.")
guests.remove("mike")
guests.append("sarah")


Print a second set of invitation messages, one for each person who is still in your list.
print(f"{guests[0].capitalize()}, you're still invited to dinner.")
print(f"{guests[1].capitalize()}, you're still invited to dinner.")
print(f"{guests[-1].capitalize()}, you're invited to dinner.")


# Use insert() to add one new guest to the beginning and middle of your list.
guests.insert(0, "theo")
guests.insert(2, "sally")


# Use append to add a guest at the end of list
guests.append("cj")


# Print a new set of invitation messages, one for each person in your list.
print(f"{guests[0].capitalize()}, you're invited to dinner.")
print(f"{guests[2].capitalize()}, you're invited to dinner.")
print(f"{guests[-1].capitalize()}, you're invited to dinner.")


# Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Print a message to each uninvited guest.
uninvited_guest_1 = guests.pop()
univited_guests_2 = guests.pop()
uninvited_guests_3 = guests.pop()
uninvited_guests_4 = guests.pop()

print(f"{uninvited_guest_1.capitalize()}, you're no longer invited.")
print(f"{univited_guests_2.capitalize()}, you're no longer invited.")
print(f"{uninvited_guests_3.capitalize()}, you're no longer invited.")
print(f"{uninvited_guests_4.capitalize()}, you're no longer invited.")


# Use del to remove the last two names from your list, so you have an empty list.
del guests[:]
