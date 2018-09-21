#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

"""A class to show Admin priviledges"""

from user_priv_admin_classes import Admin

user_priv = Admin('amy', 'haddad')
print(user_priv.priviledges_available.show_priviledges())
