#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# import entire module
import separate_file
separate_file.make_shirt('small', 'boston')

# import specific function
from separate_file import describe_city
describe_city('portland', 'united states')

# function as alias
from separate_file import make_shirt as m_s
m_s('large', 'travel')

# module as alias
import separate_file as sf
sf.make_shirt('small', 'travel widely')

# import all functions
from separate_file import *

make_shirt('small', 'i love boston')
describe_city('boston', 'united states')
