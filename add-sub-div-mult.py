#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:37:21 2021

@author: ashleygratton1
"""

a = int(input("Enter a..."))
b = int(input("Enter b..."))

list = ["add", "subtract", "multiply", "divide"]

d = input("What would you like to do? Add, subtract, multiply or divide?")


if d == 'multiply':
    output = a*b
else:
    pass 
    
if d == 'divide':
    output = a/b
else:
    pass
    
if d == 'add':
    output = a+b
else:
    pass
    
if d == 'subtract':
    output = a-b
else:
    pass

if d not in list:
    print("Error")
else:
    print("The answer to your question is",output)
