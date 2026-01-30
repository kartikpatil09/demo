print("----------------------------------SIMPLR CALCULATOR----------------------------------")
print("Welcome to the Simple Calculator!")  
print("You can perform the following operations:")
print("1. Addition (+)") 
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice(1-4) : ") 
a = float(input("Enter the first number: "))
b = float(input("enter the second number:"))
import numpy as np 

def add( a, b): 
    return a + b
def subtract( a, b): 
    return a - b        
def multiply( a, b):
    return a * b
def divide( a, b):
    if b == 0:
        print("Error: Division by zero")

    return a / b
