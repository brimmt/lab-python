"""
Title: Calculator mMiniproject
Author: Tatiana Brimm
Description:
  This is a series where I will rebuild simple projects in multiple languages to reinforce foundational basics. 
  This folder will contain mostly the logic only. The full project will be posted separately and labeled as fs-calulator-python 
  in github. 
"""



def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1,num2):

    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cant Divide by 0"
    

while True:

    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    opp = input("Choose an operator(+,-,*,/) or 'exit to quit: ")
    
    if opp.lower() == "exit":
        print("Closing calulcator, Bye!")
        break

    if opp == "+":
        result = (add(num1,num2))
    elif opp == "-":
        result = (subtract(num1,num2))
    elif opp == "*":
        result = (multiply(num1,num2))
    elif opp == "/":
        result = (divide(num1,num2))
    else:
        result = 'Invalid operator'

    print(f"Your result is: {result}")
    






