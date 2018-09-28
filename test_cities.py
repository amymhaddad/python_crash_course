#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Create a file called test_cities.py that tests the function you just wrote in 11-1
import unittest
from city_functions import city_country

class city_country_test(unittest.TestCase):
    """Test city, country format"""

    def test_city_country_combination(self):
        """See if value returns in this format: City, Country"""

        formatted_city_country = city_country('dublin', 'ireland')
        self.assertEqual(formatted_city_country, 'Dublin, Ireland')

unittest.main()


# Test the function you wrote in 11-2

import unittest
from city_functions import city_country

class CityInfoTest(unittest.TestCase):
    """Test to see if city information is formatted correctly"""

    def test_city_coutry(self):
        """Does the city, country combination look like this: 'Dublin, Ireland?'"""

        city_country_format = city_country('dublin', 'ireland')
        self.assertEqual(city_country_format, 'Dublin, Ireland')
  
    def test_city_country_population(self):
        """Does the city, country information look like this: 'Dublin, Ireland - 500000?'"""

        city_country_format = city_country('dublin', 'ireland', 500000)
        self.assertEqual(city_country_format, 'Dublin, Ireland - 500000')

unittest.main()
