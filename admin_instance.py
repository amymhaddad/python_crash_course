#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

"""A model for a user and their privledges"""

from user_class import User
from priv_and_admin_classes import Admin

user_1 = User('amy', 'haddad')
print(user_1.describe_user())

user_1_priv = Admin('amy', 'haddad')
print(user_1_priv.priviledges_available.show_priviledges())
