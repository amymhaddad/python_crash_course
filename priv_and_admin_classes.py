#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

"""Two classes that can be used to represent a user's priviledges"""

from user_class import User

class Priviledges():
    """An attempt to list the priviledges for a user"""
    def __init__(self, priviledges=['create expense reports', 'organize company meetings', 'plan company events']):
        self.priviledges = priviledges
    
    def show_priviledges(self):
        """Show the priviledges"""
        print("These are the priviledges available: ")
        for priviledge in self.priviledges:
            print(f"-{priviledge.capitalize()}")

class Admin(User):
    """An attempt to model a specific type of user, an admin"""
    def __init__(self, first_name, last_name):
        """Initialize the attributes from parent to child"""
        super().__init__(first_name, last_name)
        self.priviledges_available = Priviledges()
    