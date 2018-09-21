#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

"""A model to show a user and their priviledges"""

class User():
    """"An attempt to model a user"""
    def __init__(self, first_name, last_name):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """Summarize the user's first and last names"""
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        return full_name
    
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
    