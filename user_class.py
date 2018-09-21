#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

"""A class that can be used to represent a user"""

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