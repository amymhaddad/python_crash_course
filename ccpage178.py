#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

class Car():
    """An attempt to model a car"""

    def __init__(self, make, model, year, range):
        self.make = make
        self.model = model
        self.year = year
        self.range = range
        self.odometer_reading = 100

class Battery():
    """An attempt to provide detail about a battery for a specific car, an electric one"""

    def __init__(self, battery_size=70):
        """Initialize the attribute"""
        self.battery_size = battery_size

    def get_range(self):
        """Report the number of miles a car will get based on the battery size"""
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270

        print(f"This car can go about {self.range} miles when fully charged.")

    def upgrade_battery(self):
        """Increase the battery size"""
        if self.battery_size < 85:
            self.battery_size = 85
            upgraded_range = 270

        print(f"This car can go about {upgraded_range} miles now.")

    def describe_battery(self):
        """Write a sentence that describes the size of the battery"""
        print(f"The size of the battery is: {self.battery_size}-kWh.")

class ElecticCar(Car):
    """An attempt to model a specific type of car, an electric one"""

    def __init__(self, make, model, year, range):
        """Initialize the attributes from parent to child"""
        super().__init__(make, model, year, range)
        self.battery = Battery()


my_tesla = ElecticCar('tesla', 't1', 240, 2019)

print(my_tesla.battery.get_range())

print(my_tesla.battery.upgrade_battery())
