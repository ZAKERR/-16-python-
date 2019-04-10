# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:35:09 2018

@author: Administrator
"""

def add(a,b):
    return a + b
    
def subtraction(a,b):
    try:
        return a - b
    except(ZeroDivisionError,TypeError) as e:
        print(e)
        
def multiply(a,b):
    return a * b

def division(a,b):
    try:
        return a / b 
    except(ZeroDivisionError,TypeError) as e:
        print(e)     
while True:
    number1 = float(input('Enter the first number: '))
    number2 = float(input('Enter the second number: '))
    choice = int(input('Enter the number of operation(0: exit，1：/, 2: +, 3: -, 4: *)'))
    if choice == 1:
        print(division(number1,number2))
    elif choice == 2:
        print(add(number1,number2))
    elif choice == 3:
        print(subtraction(number1,number2))
    elif choice == 4:
        print(multiply(number1,number2))
    else:
        break
