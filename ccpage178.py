#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Write a class called IceCreamStand that inherits from the Restaurant class.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.
class Restaurant():
    """An attempt to model a restaurant"""
    def __init__(self, name, cuisine):
        """Initialize the attributes"""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """Write two sentences to describe restaurant"""
        print(f"The restaurant is called {self.name.title()}.")
        print(f"{self.name.title()} serves {self.cuisine.title()}.")
    
    def open(self):
        """Indicate whether or not the restaurant is open"""
        print(f"{self.name.title()} is open.")
    
class IceCreamStand(Restaurant):
    """An attempt to model a specific type of restaurant, an ice cream shop"""
    def __init__(self, name, cuisine):
        """Initialize the attributes"""
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']
    
    def ice_cream_flavors(self):
        """List the ice cream flavors offered"""
        flavors_offered = ['chocolate', 'vanilla', 'strawberry']
        print("These are the flavors offered: ")
        for flavor in flavors_offered:
            print("-" + flavor.title())
        

my_icecream = IceCreamStand('whits', 'ice cream')
print(my_icecream.ice_cream_flavors())



# Write a class called Admin that inherits from the User class.
# Add an attribute, privileges, that stores a list of strings like:
# "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method.
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
    
class Admin(User):
    """An attempt to model a specific type of user, an admin"""
    def __init__(self, first_name, last_name):
        """Initialize the attributes from parent to child"""
        super().__init__(first_name, last_name)
        self.priviledges = ['can add post', 'can delete post', 'can ban user']
    
    def show_admin_priviledges(self):
        """Show the list of admin priviledges"""
        print("These are the privledges of an Admin: ")
        for priviledge in self.priviledges:
            print(f"-{priviledge.capitalize()}")


user_type = Admin('tom', 'smith')

print(user_type.show_admin_priviledges())



# Based on the code above:
# Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings as described in exercise above. 
# Move the show_privileges() method to this class.
# Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.
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
    

user_type = Admin('tom', 'smith')

print(user_type.priviledges_available.show_priviledges())



# Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery.
class Car():
    """An attempt to model a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

class Battery():
    """An attempt to provide detail about a battery for a specific car, an electric one"""
    def __init__(self, battery=70):
        """Initialize the attribute"""
        self.battery = battery
    
    def get_range(self):
        """Report the number of miles a car will get based on the battery size"""
        if self.battery == 70:
            range = 240
        elif self.battery == 85:
            range = 270
        
        print(f"This car can go about {range} miles when fully charged.")

    def upgrade_battery(self):
        """Increase the battery size"""
        if self.battery < 85:
            self.battery = 85
            upgraded_range = 270
        
        print(f"This car can go about {upgraded_range} miles now.")

    def describe_battery(self):
        """Write a sentence that describes the size of the battery"""
        print(f"The size of the battery is: {self.battery}-kWh.")

class ElecticCar(Car):
    """An attempt to model a specific type of car, an electric one"""
    def __init__(self, make, model, year):
        """Initialize the attributes from parent to child"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElecticCar('tesla', 't1', 2019)

print(my_tesla.battery.get_range())

print(my_tesla.battery.upgrade_battery())
