#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:04:20 2017

@author: MyraLiu
"""

#recursion exercise
def factorial(num):
    if num == 2:
        return num
    else:
        return num * factorial(num-1)
    
print (factorial(5))


#%%
# OOP exercise

class student:
    def __init__(self, name = '', class_of = 0, major = '', knowledge = 0):
        self.name = name
        self.class_of = class_of
        self.major = major
        self.knowledge = 0
    #define the functions we will use in this class    
   
    def set_name(self, name):  #change name, called setter
        self.name = name
        
    def get_name(self):  #getter, show the value of properties
        return self.name
    
    def set_class_of(self, class_of):
        self.class_of = class_of
    
    def get_class_of(self):
        return self.class_of
    
    def study(self, time_s):
        self.knowledge += 10*time_s
    
    
