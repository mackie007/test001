#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type =cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
    def open_restaurant(self):
        print('餐馆正在营业')

class Privileges():
    def __init__(self):
        self.privileges = ["can add post" ,"can delete post" ,"can ban user"]
    def show_privileges(self):
        print(self.privileges)

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("First name is " + self.first_name.title() )
        print("Last name is " + self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print('Hello ' + full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()







