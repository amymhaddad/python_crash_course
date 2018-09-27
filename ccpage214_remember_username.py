#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import json

def get_username():

    """Get the username, if one exists"""

    filename = 'username1.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        None
    else:
        return username

def create_username():

    """Create a username, if one doesn't exist"""

    filename = 'username1.json'
    username = input("Enter your username: ")

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():

    """Greet the user and make sure the users are the same people"""

    username = get_username()

    verify_username = input(f"Is your username {username}? Type \'yes\' or \'no\'. ")

    if verify_username == 'yes':
        print(f"Welcome back, {username}!")
    else:
        username = create_username()
        print(f"We'll remember you next time, {username}.")

greet_user()

